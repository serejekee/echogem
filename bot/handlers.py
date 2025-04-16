#import logging
import random
import os
import asyncio
from aiogram import types
from aiogram.types import FSInputFile
from utils import generate_text_and_image, is_url_valid


# Настройка логирования
#logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s",)


async def handle_post(message: types.Message):
    file_path = os.path.join(os.path.dirname(__file__), 'data', 'topics.txt')
    with open(file_path, "r", encoding="utf-8") as file:
        topics = file.read().splitlines()
    topics = [topic.strip() for topic in topics if topic.strip()]

    max_attempts = 5

    for attempt in range(max_attempts):
        query = random.choice(topics)
        try:
            text, image_url = await generate_text_and_image(query)

            if text:
                if image_url and await is_url_valid(image_url):
                    await message.answer_photo(photo=image_url, caption=text)
                    return
                else:
                    fallback_path = os.path.join(os.path.dirname(__file__), 'data', 'fallback.jpg')
                    await message.answer_photo(photo=FSInputFile(fallback_path), caption=text)
                    return
        except Exception as e:
            await asyncio.sleep(3)

    await message.answer("Не удалось сгенерировать пост. Попробуйте позже.")
