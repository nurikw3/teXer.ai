from aiogram.types import (
    ReplyKeyboardMarkup,
    KeyboardButton
)

main = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Teacher'),
            KeyboardButton(text='Student')
        ]
    ],
    resize_keyboard=1,
    one_time_keyboard=1,
    input_field_placeholder='who are u',
    selective=1
)