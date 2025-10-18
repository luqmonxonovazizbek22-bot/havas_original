from aiogram import types, Router, F
from aiogram.types import FSInputFile
from keyboard.default_keyboard import main_keyboard

router = Router()


@router.message(F.text == "🏢 Biz haqimizda")
async def send_message(message: types.Message):
    video = FSInputFile("media/video.mp4")
    await message.answer_video(video=video,
                               caption="""🌠HAVAS

📌СЕТЬ ДИСКАУНТЕРОВ "У ДОМА"
Мы предлагаем нашим покупателям качественные продукты по выгодной цене. В наших магазинах представлены товары известных мировых и локальных брендов, а также товары собственного производства.""")