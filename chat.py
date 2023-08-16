import logging
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# Установка уровня логирования
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)

logger = logging.getLogger(__name__)

# Команда /start
def start(update, context):
    reply_keyboard = [['/chat', '/repo']]
    markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)

    update.message.reply_text('Привет! Я анонимный чат-бот. Что бы вы хотели сделать?',
                              reply_markup=markup)

# Команда /chat
def chat(update, context):
    update.message.reply_text('Вы вошли в анонимный чат. Все сообщения будут анонимны.')

# Команда /repo
def repo(update, context):
    update.message.reply_text('Бот создан TannicArcher\n'
                              'Репозиторий: https://github.com/TannicArcher')

# Обработка текстовых сообщений
def echo(update, context):
    update.message.reply_text('Вы: ' + update.message.text)

# Отображение ошибок
def error(update, context):
    logger.warning('Update "%s" caused error "%s"', update, context.error)

def main():
    # Токен вашего бота
    token = 'YOUR_BOT_TOKEN'

    # Создание экземпляра Updater и передача токена
    updater = Updater(token, use_context=True)

    # Получение диспетчера для регистрации обработчиков
    dp = updater.dispatcher

    # Регистрация обработчиков команд
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("chat", chat))
    dp.add_handler(CommandHandler("repo", repo))

    # Регистрация обработчика текстовых сообщений
    dp.add_handler(MessageHandler(Filters.text, echo))

    # Регистрация обработчика ошибок
    dp.add_error_handler(error)

    # Запуск бота
    updater.start_polling()

    # Остановка бота при нажатии Ctrl+C
    updater.idle()

if __name__ == '__main__':
    main()
