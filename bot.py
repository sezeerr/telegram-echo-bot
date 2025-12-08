import os
from dotenv import load_dotenv
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# загружаем токен 
load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")


def start(update, context):
    user = update.effective_user
    update.message.reply_text(
        f"Привет, {user.first_name}! Я telegram эхо-бот."
    )


def help_command(update, context):
    update.message.reply_text("Напиши мне любое сообщение — я его повторю!")


def echo(update, context):
    update.message.reply_text(update.message.text)


def main():
    if not TOKEN:
        raise RuntimeError("Ошибка: BOT_TOKEN не найден. Проверь файл .env!")

    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    # Команды
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help_command))

    # Эхо всех текстов
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

    # Запуск бота
    updater.start_polling()
    updater.idle()


if __name__ == "__main__":
    main()
