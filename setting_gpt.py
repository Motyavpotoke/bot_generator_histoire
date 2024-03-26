import requests
from config import folder_id

MAX_MODEL_TOKENS = 100
CONTINUE_STORY = ('Продолжи сюжет в 4 предложения и оставь интригу. Ты не должен писать некакой пояснительный текст от '
                  'себя')

token = ''


def contiune_text(text):
    pr = f'Пользователь продолжил сценарий: {text}, теперь продолжай сценарий ты.'

    pr += ('Продолжи сюжет в 4 предложения и оставь интригу. Ты не должен писать некакой пояснительный текст от '
           'себя')

    return pr


def count_tokens(text):
    headers = {
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json'
    }
    data = {
        "modelUri": f"gpt://{folder_id}/yandexgpt-lite/latest",
        "maxTokens": MAX_MODEL_TOKENS,
        "text": text
    }
    return len(
        requests.post(
            "https://llm.api.cloud.yandex.net/foundationModels/v1/tokenize",
            json=data,
            headers=headers
        ).json()['tokens']
    )


def create_prompt(info1, info2, info3, info4):
    prompt = ('Ты пишешь историю вместе с человеком. Историю надо писать по очереди. Первым начинает писать историю '
              'человек'
              'а ты продолжаешь. Если в диалоге уместно добавлять диалоги между персонажами то ты можешь их добавлять. '
              'Диалоги нужно писать с новой строки и отделяй тире. Не нужно писать пояснительный текст в начале, а'
              'просто логично продолжай историю')

    prompt += (f"Напиши начало истории в стиле {info1} "
               f"с главным героем {info2}. "
               f"Вот начальный сеттинг: {info3}. "
               "Начало должно быть коротким, 4 предложения.")

    if info4 is None:
        prompt += f'Также пользователь написал какую дополнительную информацию нужно учесть: {info4}'

    prompt += 'Не пиши некакие подсказки пользователю, так как он сам знает что он делает и ему не нужны подсказки.'

    return prompt
