from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

# Асинхронная функция обработки команды /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text('Hello!')

# Основная функция для инициализации бота
def main() -> None:
    API_TOKEN = '8170771999:AAEHn3A6pVoFMRy91bfcQz7RYqtKYeByhvY'
    
    # Создаем объект Application вместо Updater
    application = Application.builder().token(API_TOKEN).build()

    # Добавляем обработчик команды /start
    application.add_handler(CommandHandler('start', start))

    # Запускаем бота
    application.run_polling()

if __name__ == '__main__':
    main()
