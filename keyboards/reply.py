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

done = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='✅ done'),
        ]
    ],
    resize_keyboard=1,
    one_time_keyboard=1,
    input_field_placeholder='When you are done, click on the button',
    selective=1
)