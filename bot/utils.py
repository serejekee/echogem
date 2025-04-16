import os
#import logging
import google.generativeai as genai
import aiohttp

# Настройка логирования
#logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s",)

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel('gemini-2.0-flash')


async def is_url_valid(url: str) -> bool:
    async with aiohttp.ClientSession() as session:
        try:
            async with session.head(url) as response:
                is_valid = response.status == 200
                return is_valid
        except Exception as e:
            return False


async def generate_text_and_image(query: str, max_attempts=3):
    for attempt in range(1, max_attempts + 1):
        file_path = os.path.join(os.path.dirname(__file__), 'data', 'prompt.txt')
        with open(file_path, "r", encoding="utf-8") as file:
            prompt_template = file.read()
        prompt = prompt_template.format(query=query)

        try:
            response = model.generate_content(prompt)

            if response and response.parts:
                full_text = response.text.strip()

                if ' : ' in full_text:
                    text_part, image_url = map(str.strip, full_text.rsplit(" : ", 1))
                    if text_part and image_url:
                        return text_part, image_url
                    else:
                        continue
                else:
                    continue
            else:
                continue

        except Exception as e:
            continue

    return "", ""


