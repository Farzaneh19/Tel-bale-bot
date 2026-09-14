# 🎓 Tel-bale-bot
### ربات تلگرام و بله برای مدیریت ارائه‌های دانشجویی
### Telegram & Bale Bot for University Presentation Management

---

## 🇮🇷 معرفی (Introduction)
این ربات برای خودکارسازی فرآیند انتخاب موضوعات ارائه در کلاس‌های دانشگاهی طراحی شده است. این ابزار به دانشجویان اجازه می‌دهد تا به راحتی موضوعات موجود را مشاهده و رزرو کنند، و به استاد یا نماینده کلاس امکان مدیریت و خروجی‌گیری از لیست ثبت‌نامی‌ها را می‌دهد.

This bot is designed to automate the process of selecting presentation topics for university classes. It allows students to easily view and reserve available topics, while enabling instructors or class representatives to manage and export the registration list.

---

## 🚀 ویژگی‌ها (Features)

*   **مدیریت داینامیک (Dynamic Management):** امکان آپلود فایل اکسل (`topics.xlsx`) جهت تعریف موضوعات جدید.
*   **رزرو هوشمند (Smart Reservation):** جلوگیری از تداخل (هر موضوع فقط توسط یک نفر انتخاب می‌شود).
*   **گزارش‌گیری (Admin Export):** دریافت خروجی اکسل از تمامی ثبت‌نامی‌ها با دستور `/export` توسط ادمین.
*   **امنیت (Security):** استفاده از متغیرهای محیطی برای حفاظت از توکن‌ها (`.env`).

---

## 🛠 تکنولوژی‌های استفاده شده (Tech Stack)

*   **Language:** Python 3.x
*   **Library:** `python-telegram-bot`
*   **Data Handling:** `pandas`, `openpyxl`
*   **Environment:** `python-dotenv`
*   **Deployment:** RunFlare Cloud

---
   
