from aiogram.utils.keyboard import ReplyKeyboardMarkup, KeyboardButton


def main_keyboard():
    button = KeyboardButton(text="🏢 Biz haqimizda")
    button2 = KeyboardButton(text="💼 Ariza qoldiring")
    button3 = KeyboardButton(text="📞 Kontaktlar")
    button4 = KeyboardButton(text="💬 Qayta aloqa")
    button5 = KeyboardButton(text="🇺🇿/🇷🇺 Tilni o'zgartirish")
    rkm = ReplyKeyboardMarkup(
        keyboard=[
            [button],
            [button2],
            [button3, button4],
            [button5],
        ],
        resize_keyboard=True
    )
    return rkm



def ariza_keyboard():
    button = KeyboardButton(text="Markaziy ofis")
    button2 = KeyboardButton(text="Sirdaryo")
    button3 = KeyboardButton(text="↪️Bosh menyu")
    button4 = KeyboardButton(text="Toshkent")
    button5 = KeyboardButton(text="Toshkent viloyati")
    button6 = KeyboardButton(text="⬅️Orqaga")
    rkm = ReplyKeyboardMarkup(
        keyboard=[
            [button,button2],
            [button3,button4],
            [button5, button6],
        ],
        resize_keyboard=True
    )
    return rkm