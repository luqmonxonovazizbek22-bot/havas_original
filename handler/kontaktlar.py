from aiogram import types, Router, F
from keyboard.default_keyboard import main_keyboard

router = Router()


@router.message(F.text == "📞 Kontaktlar")
async def send_message(message: types.Message):
    havasph = "https://ik.imagekit.io/3zhf1wjym/photo_2025-10-01_20-52-28.jpg?updatedAt=1759410693427"
    await message.answer_photo(photo=havasph,
                               reply_markup=media_inline(),
                               caption="""🤝Для связи:
☎️Контакты +998 71 205 95 95
📩Электронная почта havas_uz@mail.ru""")