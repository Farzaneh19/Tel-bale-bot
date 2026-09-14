import os
import logging
import pandas as pd
from dotenv import load_dotenv
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    ApplicationBuilder, CommandHandler, CallbackQueryHandler,
    MessageHandler, filters, ContextTypes
)

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")
ADMIN_ID = int(os.getenv("ADMIN_ID", 0))

TOPICS_FILE = "topics.xlsx"
REGISTRATIONS_FILE = "registrations.xlsx"


def load_all_topics():
    if not os.path.exists(TOPICS_FILE): return []
    df = pd.read_excel(TOPICS_FILE)
    return df.iloc[:, 0].dropna().astype(str).tolist()


def get_reserved_topics():
    if not os.path.exists(REGISTRATIONS_FILE): return []
    df = pd.read_excel(REGISTRATIONS_FILE)
    return df["Topic"].tolist()


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    all_topics = load_all_topics()
    reserved = get_reserved_topics()
    available = [t for t in all_topics if t not in reserved]

    if not available:
        await update.message.reply_text("تمامی موضوعات رزرو شده‌اند.")
        return

    keyboard = [[InlineKeyboardButton(t, callback_data=f"sel_{i}")] for i, t in enumerate(available)]
    context.user_data["available"] = available
    await update.message.reply_text("یکی از موضوعات را انتخاب کنید:", reply_markup=InlineKeyboardMarkup(keyboard))


async def handle_selection(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    idx = int(query.data.split("_")[1])
    available = context.user_data.get("available", [])

    if idx >= len(available):
        await query.edit_message_text("خطا! لطفاً مجدد /start را بزنید.")
        return

    chosen = available[idx]

    df = pd.read_excel(REGISTRATIONS_FILE) if os.path.exists(REGISTRATIONS_FILE) else pd.DataFrame(
        columns=["User", "Topic"])
    new_data = pd.DataFrame([{"User": query.from_user.full_name, "Topic": chosen}])
    df = pd.concat([df, new_data], ignore_index=True)
    df.to_excel(REGISTRATIONS_FILE, index=False)

    await query.edit_message_text(f"✅ انتخاب شد: {chosen}")


async def export(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_user.id != ADMIN_ID: return
    if os.path.exists(REGISTRATIONS_FILE):
        await update.message.reply_document(document=open(REGISTRATIONS_FILE, "rb"))


async def upload_topics(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_user.id != ADMIN_ID: return
    file = await update.message.document.get_file()
    await file.download_to_drive(TOPICS_FILE)
    await update.message.reply_text("موضوعات بروزرسانی شد.")


if __name__ == '__main__':
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("export", export))
    app.add_handler(CallbackQueryHandler(handle_selection))
    app.add_handler(MessageHandler(filters.Document.ALL, upload_topics))
    print("Bot is running...")
    app.run_polling()
