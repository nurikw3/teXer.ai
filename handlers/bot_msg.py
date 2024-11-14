import asyncio
import os
from aiogram import Router, F
from aiogram.types import Message
import google.generativeai as genai

router = Router()
GOOGLE_API_KEY = 'AIzaSyDEVMep2BaFNpLYMNPVIIGRc0LGYQtVAFY'
genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel("gemini-1.5-flash")


#! INLINE TEACHER / STUDENT
@router.message(F.text)
async def process(msg: Message):
    msg_ = msg.text.lower()
    if msg_ == 'teacher':
        await msg.answer('test')

@router.message(F.photo)
async def handle_ph(msg: Message):
    await msg.answer('[INFO] +image has added')
    photo = msg.photo[-1]
    file_info = await msg.bot.get_file(photo.file_id)

    photo_dir = 'photos'
    if not os.path.exists(photo_dir):
        os.makedirs(photo_dir)

    photo_path = f"{photo_dir}/{photo.file_id}.jpg"


    await msg.bot.download_file(file_info.file_path, destination=photo_path)

    uploaded_file = await genai.upload_file(photo_path)
    result = await model.generate_content(prompt=[uploaded_file, "Это домашняя работа проверь ошибки если нащел скажи где не пиши лишнего"])
    
    await msg.answer("Изображение загружено, начинаю обработку...")
    print(result)

    # await message.answer("Обработка завершена.")

# async def process_image(image_path):
#     try:
#         print('PROCESSING')
#         uploaded_file = await asyncio.to_thread(genai.upload_file, image_path)
#         print('Файл загружен')

#         result = await asyncio.to_thread(
#             model.generate_content,
#             prompt=[uploaded_file, "Это домашняя работа проверь ошибки если нащел скажи где не пиши лишнего"]
#         )
#         print('Обработка завершена')
#         return result.text
#     except Exception as e:
#         print(f"Ошибка при обработке изображения: {e}")
#         return None


# @router.message(F.photo)
# async def handle_photo(message: Message):
    # await message.answer("Получаю изображение...")

    # photo = message.photo[-1]
    # file_info = await message.bot.get_file(photo.file_id)

    # # Проверяем, существует ли директория, если нет, создаем ее
    # photo_dir = 'photos'
    # if not os.path.exists(photo_dir):
    #     os.makedirs(photo_dir)

    # photo_path = f"{photo_dir}/{photo.file_id}.jpg"
    # await message.bot.download_file(file_info.file_path, destination=photo_path)
    # await message.answer("Изображение загружено, начинаю обработку...")

    # result_text = await process_image(photo_path)

    # if result_text:
    #     await message.answer(f"Описание фото: {result_text}")
    # else:
    #     await message.answer("Произошла ошибка при обработке изображения.")
    
    # os.remove(photo_path)
    # await message.answer("Обработка завершена.")



# @router.message(F.photo)
# async def handle_photo(message: Message):
    # photo = message.photo[-1]
    # file_info = await message.bot.get_file(photo.file_id)
    
    # # Проверяем, существует ли директория, если нет, создаем ее
    # photo_dir = 'photos'
    # if not os.path.exists(photo_dir):
    #     os.makedirs(photo_dir)
    
    # photo_path = f"{photo_dir}/{photo.file_id}.jpg"
    # await message.bot.download_file(file_info.file_path, destination=photo_path)
    # result_text = await process_image(photo_path)

    # if result_text:
    #     await message.answer(f"Описание фото: {result_text}")
    # else:
    #     await message.answer("Произошла ошибка при обработке изображения.")
    
    # # os.remove(photo_path)