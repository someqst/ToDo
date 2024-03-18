from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command
from data.kb_builder import kb_build


router = Router()


@router.message(Command('start'))
async def start_cmd(message: Message):
    await message.answer('Привет, это твой ToDo бот. Начнем трахать это программирование', reply_markup=kb_build().as_markup())

