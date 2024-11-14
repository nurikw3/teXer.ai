import os
import asyncio
from aiogram import Router, F
from aiogram.types import Message
import google.generativeai as genai

GOOGLE_API_KEY = 'AIzaSyDEVMep2BaFNpLYMNPVIIGRc0LGYQtVAFY'
genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel("gemini-1.5-flash")


async def process_image(image_path):
    try:
        print('PROCESSING')
        uploaded_file = await asyncio.to_thread(genai.upload_file, image_path)
        
        result = await asyncio.to_thread(
            model.generate_content,
            prompt=[uploaded_file, "Это домашняя работа проверь ошибки если нащел скажи где не пиши лишнего"]
        )
        return result.text
    except Exception as e:
        print(f"Ошибка при обработке изображения: {e}")
        return None
