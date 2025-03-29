import asyncio
import os
from aiogram import Router, F
from aiogram.types import Message
import google.generativeai as genai
from PIL import Image
from collections import defaultdict
from aiogram.enums import ParseMode
from google.generativeai.types import RequestOptions
from google.api_core import retry
from keyboards import reply
from config_reader import config


import data.db as db


router = Router()
GOOGLE_API_KEY = config.API.get_secret_value()
genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel("gemini-1.5-pro")



photo_queue = defaultdict(list)



@router.message(F.photo)
async def handle_ph(msg: Message):

    
    user_id = msg.from_user.id
    user_status = await db.get_user_status(user_id=user_id)
    print('[+] image received')
    #! FOR TEACHER
    if user_status == 'teacher':
        photo = msg.photo[-1]
        file_info = await msg.bot.get_file(photo.file_id)
        
        photo_dir = 'photos'
        if not os.path.exists(photo_dir):
            os.makedirs(photo_dir)
        
        photo_path = f"{photo_dir}/{photo.file_id}.jpg"
        await msg.bot.download_file(file_info.file_path, destination=photo_path)
        
        if msg.caption:
            comment = msg.caption

        photo_queue[user_id].append({'photo_path': photo_path, 'comment': comment})
        await msg.answer("[+] The photo has been added", reply_markup=reply.done)

        print(photo_queue)


#! REPLY TEACHER / STUDENT
@router.message(F.text)
async def process(msg: Message):
    msg_ = msg.text.lower()


    if msg_ == 'teacher':
        
        await msg.answer('Now your status is Teacher\ncongr!🎉')
        await db.add_user(msg.from_user.id, 'teacher')
    elif msg_ == 'student':
        await msg.answer('Now your status is Student\ncongr!🎉')
        await db.add_user(msg.from_user.id, 'student')


    elif msg_ == '✅ done':
        user_id = msg.from_user.id
        print('queue!')
        if user_id not in photo_queue or not photo_queue[user_id]:
            await msg.answer("Нет фото для обработки.")
            return
        
        responses = []
        for item in photo_queue[user_id]:
            photo_path = item['photo_path']
            comment = item['comment']

            img = Image.open(photo_path)
            response = await model.generate_content_async([f'Student: {comment}. He is right?', img], request_options=RequestOptions(retry=retry.Retry(initial=10, multiplier=2, maximum=60, timeout=300)))
            responses.append(f"{comment}: {response.parts[0].text}")
        for response in responses:
            await msg.answer(response)

        # full = await model.generate_content_async(f'Анализируй данный список учеников и как их ИИ оценил. Сделай общую оценку учеников кратко, где много ошибаются где нужны доработки и тд вот сам список {responses}')
        # print(full)
        # formatted_responses = "\n".join(responses)
        # print(formatted_responses)
        # full_analysis = await model.generate_content_async(
        # f'Анализируй данный список учеников и как их ИИ оценил. Сделай общую оценку учеников кратко, где много ошибаются, где нужны доработки и тд вот сам список:\n{formatted_responses}'
        # )
        # print(full_analysis)  # Debugging the full analysis

        # Send the analysis to the teacher
        # await msg.answer(f"Общий анализ:\n{full_analysis.parts[0].text}")

        del photo_queue[user_id]
        await msg.answer("Обработка завершена.")