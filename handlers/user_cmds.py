from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command, CommandObject, CommandStart

from keyboards import reply 
import data.db as db 
router = Router()

@router.message(CommandStart())
async def start(msg: Message):
    id: int = msg.from_user.id
    user_exist = await db.user_exists(id)
    if user_exist:
        user_status = await db.get_user_status(user_id=id)
        if user_status == 'teacher':
            await msg.answer("Your status is a Teacher.\nA quick guide for you: take off a photo with a comment on the student's name.\nWhen you're done, press done on the keyboard")
    else:
        await msg.answer(f'Hello {msg.from_user.full_name}!\nWelcome to teXeris.ai ! First, select your status so that the AI can help with a particular task', reply_markup=reply.main)