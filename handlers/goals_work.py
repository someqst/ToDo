import json
import random
from loader import bot
from aiogram import F, Router
from aiogram.types import CallbackQuery, Message
from aiogram.filters import Command
from data.kb_builder import kb_build


router = Router()


@router.message(Command('add'))
async def add_goal(message: Message):
    info = await reading_file()
    
    goals = info['goals']

    goals.append(message.text[4:])

    with open('data/goals.json', 'w', encoding='utf-8') as file:
        json.dump(
            {"goals": goals},
            file,
            ensure_ascii=False
        )
    await message.answer('Добавлено', reply_markup=kb_build().as_markup())
    


@router.callback_query(lambda call: call.data not in ('add_goal'))
async def mark_goal(call: CallbackQuery):
    await call.answer()
    await set_number(1)
    info = await reading_file()
    
    goals = info['goals']

    goals.pop(int(call.data))

    with open('data/goals.json', 'w', encoding='utf-8') as file:
        json.dump(
            {"goals": goals},
            file,
            ensure_ascii=False
        )
    
    await call.message.edit_reply_markup(reply_markup=kb_build().as_markup())


async def send_summary():
    info = await reading_file()
    if info['goals'] == 0:
        await bot.send_message(539937958, 'Ты дура или дебик? У тебя были сутки, чтобы сделать что-то, но ты все просрал')
    else:
        await set_number(0)
        gifts = ('шоколадку', 'Марс', 'Чизболс', 'Любую вкусняшку', 'Конфеты на выбор')
        await bot.send_message(539937958, f'Ура, ты молодец, сделал хоть что-то, чтобы стать лучше. Разрешаю тебе купить {random.choice(gifts).lower()}')


async def send_goals():
    info = (await reading_file())['goals']
    if info:
        await bot.send_message(539937958, f'Задачи на сегодня:\n{str(", ".join(info))}', reply_markup=kb_build().as_markup())
    else:
        await bot.send_message(539937958, f'Добавь задачу, развивайся')


async def send_messages():
    messages = ('Давай-давай, поднажми', 'Я понимаю, что соблазн сидеть на ЗП велик, но нужно развиваться',
                 'Да ладно тебе, скоро никому нужен не будешь', 'Когда я делал бота, то верил в себя. Сейчас тоже верю',
                 'У тебя все получится, ты получишь свой оффер.')
    await bot.send_message(539937958, random.choice(messages))


async def reading_file():
    with open('data/goals.json', 'r', encoding='utf-8') as file:
        info = json.load(file)
    return info


async def set_number(num):
    with open('data/done_goals.json', 'w', encoding='utf-8') as file:
        json.dump(
            {"done_or_not": num}, 
            file
        )
    