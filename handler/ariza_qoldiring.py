from aiogram import types, Router, F
from aiogram.types import FSInputFile
from keyboard.default_keyboard import main_keyboard, ariza_keyboard

router = Router()


@router.message(F.text == "💼 Ariza qoldiring")
async def send_message(message: types.Message):
    await message.answer(text="Sizni rezyumeingizni to'ldirishni boshlaymiz")
    await message.answer(
        text="📍 Viloyatni tanlang",
        reply_markup=ariza_keyboard()
    )

@router.message(F.text == "⬅️Orqaga")
async def send_message(message: types.Message):
        await message.answer(text="Orqa",
                             reply_markup=main_keyboard())




