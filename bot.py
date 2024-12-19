from telegram.ext import ApplicationBuilder, MessageHandler
from telegram import Update
from telegram.ext import ContextTypes, filters

# ضع رمز الـ API الخاص بك هنا
TOKEN = "6243650306:AAHSCTWLd2nNQhTtFOIfhH2puFqU3eVUzcA"

# الدالة التي تتعامل مع الرسائل
async def auto_reply(update: Update, context: ContextTypes.DEFAULT_TYPE):
    reply = "https://t.me/mena_support تواصل هنا فقط"
    await update.message.reply_text(reply)

# إعداد البوت
def main():
    # إنشاء التطبيق وربط التوكن
    app = ApplicationBuilder().token(TOKEN).build()

    # إضافة معالج للرسائل النصية
    app.add_handler(MessageHandler(filters.TEXT, auto_reply))

    print("البوت يعمل الآن...")
    app.run_polling()

if __name__ == "__main__":
    main()
