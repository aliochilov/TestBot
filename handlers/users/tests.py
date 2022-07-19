from aiogram import types

from keyboards.default.fanlar import tests
from loader import dp, bot


@dp.message_handler(content_types=types.ContentType.DOCUMENT)
async def dars(message: types.Message):
    await message.reply(message.document.file_id)


@dp.message_handler(text="Testlar")
async def test(message: types.Message):
    await message.answer(f"Fani tanlang", reply_markup=tests)


@dp.message_handler(text="📖Matematika")
async def test(message: types.Message):
    document_id = 'BQACAgIAAxkBAAMWYtaQUCYQgco4Jjd6cGnntFhL7WYAAlMdAAKOUrBKPEOFXFY489UpBA'
    await bot.send_document(message.chat.id, document=document_id)

msg = f"Xozircha bizda bu fandan test yuq"

@dp.message_handler(text="📚Ona-tili")
async def test(message: types.Message):
    await message.answer(msg)

@dp.message_handler(text="📐Fizika")
async def test(message: types.Message):
    await message.answer(msg)


@dp.message_handler(text="🌏Geografiya")
async def test(message: types.Message):
    await message.answer(msg)


@dp.message_handler(text="🏛Tarix")
async def test(message: types.Message):
    await message.answer(msg)

