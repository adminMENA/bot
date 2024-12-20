from telegram.ext import ApplicationBuilder, MessageHandler
from telegram import Update
from telegram.ext import ContextTypes, filters
import os  # استيراد مكتبة os للحصول على المنفذ من البيئة

# ضع رمز الـ API الخاص بك هنا
TOKEN = "6243650306:AAHSCTWLd2nNQhTtFOIfhH2puFqU3eVUzcA"

# الدالة التي تتعامل مع الرسائل
async def auto_reply(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message:  # تحقق من وجود رسالة
        reply = "https://t.me/mena_support تواصل هنا فقط"
        await update.message.reply_text(reply)

# إعداد البوت
def main():
    # إنشاء التطبيق وربط التوكن
    app = ApplicationBuilder().token(TOKEN).build()

    # إضافة معالج للرسائل النصية
    app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), auto_reply))

    print("البوت يعمل الآن...")

    # الحصول على المنفذ من البيئة
    port = int(os.environ.get('PORT', 8443))

    # إعداد Webhook
    app.run_webhook(
        listen="0.0.0.0",
        port=port,
        webhook_url=f"https://bot.onrender.com/{TOKEN}"  # الرابط المعدّل ليطابق اسم تطبيقك
    )

if __name__ == "__main__":
    main()
