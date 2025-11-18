import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters, ConversationHandler

# Етапи розмови
NAME, CONTACT, COMMENT = range(3)

# Старт команди
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Привіт! Щоб подати заявку на вакансію, напиши своє ім’я."
    )
    return NAME

# Отримуємо ім'я
async def get_name(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data['name'] = update.message.text
    await update.message.reply_text("Введіть свій контакт (Telegram, Viber, Email):")
    return CONTACT

# Отримуємо контакт
async def get_contact(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data['contact'] = update.message.text
    await update.message.reply_text("Додайте коментар або посилання на резюме:")
    return COMMENT

# Отримуємо коментар/резюме
async def get_comment(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data['comment'] = update.message.text

    # Надсилаємо заявку адміністратору
    7837437860 = int(os.environ.get("7837437860"))
    await context.bot.send_message(
        chat_id=7837437860,
        text=f"Нова заявка:\nІм’я: {context.user_data['name']}\nКонтакт: {context.user_data['contact']}\nРезюме/Коментар: {context.user_data['comment']}"
    )

    await update.message.reply_text("Дякуємо! Ваша заявка прийнята.")
    return ConversationHandler.END

# Відміна
async def cancel(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Заявка скасована.")
    return ConversationHandler.END

# Основна функція
if __name__ == '__main__':
    8404301807:AAHuB3O8J8zvUYlGooyA7svme4z0w_K4WvY = os.environ.get("8404301807:AAHuB3O8J8zvUYlGooyA7svme4z0w_K4WvY")
    application = ApplicationBuilder().token(8404301807:AAHuB3O8J8zvUYlGooyA7svme4z0w_K4WvY).build()

    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],
        states={
            NAME: [MessageHandler(filters.TEXT & ~filters.COMMAND, get_name)],
            CONTACT: [MessageHandler(filters.TEXT & ~filters.COMMAND, get_contact)],
            COMMENT: [MessageHandler(filters.TEXT & ~filters.COMMAND, get_comment)],
        },
        fallbacks=[CommandHandler('cancel', cancel)]
    )

    application.add_handler(conv_handler)
    application.run_polling()

