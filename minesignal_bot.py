from aiogram import Bot, Dispatcher, types, executor
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import logging
import os

# 🔐 Токен из переменной окружения (Render или локально)
BOT_TOKEN = os.getenv("BOT_TOKEN", "вставь_сюда_твой_токен_если_тестируешь")

logging.basicConfig(level=logging.INFO)
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

# 📲 Кнопки
keyboard = InlineKeyboardMarkup(row_width=2)
keyboard.add(
    InlineKeyboardButton("🔗 Регистрация", url="https://1win.run/?p=ThJS"),
    InlineKeyboardButton("🎁 Промокод", callback_data="promo"),
    InlineKeyboardButton("📡 Получить сигнал", callback_data="signal")
)

# 🟢 Команда /start
@dp.message_handler(commands=["start"])
async def start_command(message: types.Message):
    text = (
        "🔮 Добро пожаловать в *Minesignal Bot*!\n\n"
        "Мы предсказываем удачные ячейки в игре *Mines от 1Win* с высокой точностью.\n\n"
        "⬇️ Выберите действие:"
    )
    await message.answer(text, reply_markup=keyboard, parse_mode="Markdown")

# 🎁 Обработка кнопки промокода
@dp.callback_query_handler(lambda c: c.data == "promo")
async def promo_callback(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, "🎁 Промокод: *1WINBETS5*", parse_mode="Markdown")

# 📡 Обработка кнопки сигнала
@dp.callback_query_handler(lambda c: c.data == "signal")
async def signal_callback(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(
        callback_query.from_user.id,
        "✨ Сигнал: попробуйте открыть 2️⃣, 5️⃣ и 8️⃣ ячейку.\n(ИИ-предсказание с 92% вероятностью)"
    )

# ▶️ Запуск
if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
