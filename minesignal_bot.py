import logging
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# ВСТАВЬ СЮДА СВОЙ ТОКЕН от BotFather
API_TOKEN = 8066551112:AAEfaHXwkOR6t4Vs9OuER_fqIvRKqx68SpQ

# Логирование
logging.basicConfig(level=logging.INFO)

# Инициализация бота
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

# Кнопка
keyboard = InlineKeyboardMarkup(row_width=1).add(
    InlineKeyboardButton("Играть в Mines 💣", url="https://1wnmjv.life/casino/play/256-mines?tag=365275"),
)

# Обработка команды /start
@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.answer("🎯 Привет! Вот сигнал для 1WIN MINES:\n\n"
                         "🟦🟦🟦\n"
                         "🟦💣🟦\n"
                         "🟦🟦🟦\n\n"
                         "Жми кнопку ниже и начинай!", reply_markup=keyboard)

# Запуск
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
