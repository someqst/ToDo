import json
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types.inline_keyboard_button import InlineKeyboardButton


def kb_build() -> InlineKeyboardBuilder:
    with open('data/goals.json', 'r', encoding='utf-8') as file:
        info = json.load(file)


    builder = InlineKeyboardBuilder([[]])

    for number, goal in enumerate(info['goals']):
        builder.button(text=f'{goal}', callback_data=f'{number}')
    
    builder.adjust(2)
    return builder