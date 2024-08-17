from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes
from telegram import Update
import nltk
from nltk.chat.util import Chat, reflections
from pairs import pairs  # Импортируйте pairs из файла pairs.py
from mistakes import correct_spelling # Импорт исправителя ошибок
import logging

logging.basicConfig(level=logging.INFO)



# Создание чат-бота
chat_bot = Chat(pairs, reflections)

TELEGRAM_TOKEN = '7346014397:AAEG_glgc5w32Ey5pTIecGRbkC7TlmI4Mvw'


async def start(update, context):
    user = update.message.from_user
    first_name = user.first_name
    last_name = user.last_name or ""
    full_name = f"{first_name} {last_name}".strip()
    greeting_message = f'Привет, {full_name}! я бот xbt, на какие вопросы вы хотели бы получить ответ?'
    await update.message.reply_text(greeting_message)


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        user_message = update.message.text
        logging.info(f"Received message: {user_message}")

        # Исправление орфографических ошибок
        corrected_message = correct_spelling(user_message)
        logging.info(f"Corrected message: {corrected_message}")

        # Получение ответа от чат-бота
        response = chat_bot.respond(corrected_message)
        logging.info(f"Bot response: {response}")

        # Отправка ответа пользователю
        await update.message.reply_text(response)
    except Exception as e:
        logging.error(f"An error occurred: {e}")
        await update.message.reply_text("Произошла ошибка. Попробуйте еще раз.")


def main():
    application = ApplicationBuilder().token(TELEGRAM_TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    application.run_polling()



if __name__ == '__main__':
    main()
