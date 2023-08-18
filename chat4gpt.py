import os
from dotenv import load_dotenv
import openai

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")
openai.api_base = "https://chimeragpt.adventblocks.cc/api/v1"
openai.api_image = "https://chimeragpt.adventblocks.cc/v1/images/generations"


def chatgpt(request='hello'):
    try:
        response_text = ""
        response = openai.ChatCompletion.create(
            model='gpt-4',
            messages=[
                {'role': 'user', 'content': request},
            ],
            stream=True
        )
        for chunk in response:
            response_text += chunk.choices[0].delta.get('content', '')
        return response_text
    except Exception as e:
        try:
            response_text = ""
            response = openai.ChatCompletion.create(
                model='gpt-3.5-turbo-16k',
                messages=[
                    {'role': 'user', 'content': request},
                ],
                stream=True
            )
            for chunk in response:
                response_text += chunk.choices[0].delta.get('content', '')
            return response_text + f'\nВ связи с ошибкой' \
                                   f'\n{e}' \
                                   f'\nОтвет был сгенерирован с использованием "gpt-3.5-turbo-16k"'
        except Exception as e:
            response_text = f'Ошибка {e}'
            return response_text


def image_generation(request='Cute anime girl', scale='1024x1024'):
    response = openai.Image.create(
        prompt=request,
        n=1,
        size=scale
    )
    image_url = response['data'][0]['url']
    return image_url


if __name__ == '__main__':
    image_generation()
