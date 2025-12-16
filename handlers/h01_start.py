from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message

from keyboards.start_kb import hello_kb

router = Router()

@router.message(Command('start'))
async def start(message: Message):
    await message.answer(text='Вызов кнопки', reply_markup=hello_kb())

@router.message(F.text == 'Приветствую')
async def hello(message: Message):
    first_name = message.from_user.first_name

    await message.answer(text=f'Привет, {first_name}.')