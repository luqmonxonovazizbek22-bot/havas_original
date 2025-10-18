from aiogram.utils.keyboard import InlineKeyboardMarkup, InlineKeyboardButton


def about_inline():
    button = InlineKeyboardButton(text="Fullname", callback_data="fullname")
    button2 = InlineKeyboardButton(text="Photo", callback_data="photo")
    button3 = InlineKeyboardButton(text="Job", callback_data="job")
    button4 = InlineKeyboardButton(text="⬅️ Back", callback_data="back")
    ikm = InlineKeyboardMarkup(
        inline_keyboard=[
            [button, button2, button3],
            [button4]
        ]
    )
    return ikm


def photo_inline():
    button = InlineKeyboardButton(text="👍 Like", callback_data="like")
    button2 = InlineKeyboardButton(text="👎 Dislike", callback_data="dislike")
    button3 = InlineKeyboardButton(text="⬅️ Back", callback_data="back2")
    ikm = InlineKeyboardMarkup(
        inline_keyboard=[
            [button, button2],
            [button3]
        ]
    )
    return ikm


def media_inline():
    button = InlineKeyboardButton(text="Facebook", url="https://www.facebook.com/havasuz/")
    button2 = InlineKeyboardButton(text="Web-site", url="https://havasfood.uz/en/")
    button3 = InlineKeyboardButton(text="Instagram", url="https://www.instagram.com/havasuz/")

    ikm = InlineKeyboardMarkup(
        inline_keyboard=[
            [button, button2,],
            [button3]
        ]
    )
    return ikm


