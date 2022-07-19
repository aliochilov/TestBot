from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from keyboards.default.menuKeyboards import menu
from loader import dp


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"Salom, {message.from_user.full_name}! \nTestlarBotga xush kelibsiz \nBizda barcha fanlardan testlar bor"
    f"\nTest yechishni boshlash uchun Testlar tugmasini bosing" , reply_markup=menu)
