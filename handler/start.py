from aiogram import types, Router
from aiogram.filters import Command

from keyboard.default_keyboard import main_keyboard

router = Router()
photo_logo = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ4okncbKk-ZowS9BVJt0yxpcJ1McUduk2iLQ&s"

@router.message(Command("start"))
async def send_message(message: types.Message):
    await message.answer_photo(photo=photo_logo,
                               caption="""Приветствую Вас, я HR-бот Havas

🤖Я:
- расскажу Вам о компании и о преимуществах работы у нас;
- помогу найти актуальные вакансии и заполнить анкету.

_______________________________________

Xush kelibsiz, men HR-bot Havas

🤖Men:
- sizga kompaniya haqida va biz bilan ishlashning afzalliklari haqida gapirib beraman;
- mavjud vakansiyalarni topishga va so'rovnomani to'ldirishga yordam beraman.""",
                               reply_markup=main_keyboard())