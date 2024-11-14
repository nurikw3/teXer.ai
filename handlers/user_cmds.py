from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command, CommandObject, CommandStart

from keyboards import reply 

router = Router()

@router.message(CommandStart())
async def start(msg: Message):
    await msg.answer(f'Salemetsizbe {msg.from_user.full_name}', reply_markup=reply.main)