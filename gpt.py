import requests
import logging
from config import folder_id
from errors import error666

token = ''


class Question_gpt2:
    def __init__(self):
        self.max_tokens = 80

    def promt(self, text):
        try:

            headers = {
                'Authorization': f'Bearer {token}',
                'Content-Type': 'application/json'
            }
            data = {
                "modelUri": f"gpt://{folder_id}/yandexgpt-lite",
                "completionOptions": {
                    "stream": False,
                    "temperature": 0.6,
                    "maxTokens": self.max_tokens

                },
                "messages": [
                    {
                        "role": "user",
                        "text": text
                    }
                ]
            }
            response = requests.post("https://llm.api.cloud.yandex.net/foundationModels/v1/completion",
                                     headers=headers,
                                     json=data)

            if response.status_code == 200:
                text = response.json()["result"]["alternatives"][0]["message"]["text"]
                print(text)
                return text
            else:
                raise RuntimeError(
                    'Invalid response received: code: {}, message: {}'.format(
                        {response.status_code}, {response.text}
                    )
                )

        except Exception as e:
            error_gpt1 = error666
            logging.error(str(e))
            return error_gpt1


class Continue_text_gpt:
    def __init__(self):
        self.max_tokens = 80

    def promt(self, text, user, CONTINUE_STORY):
        try:

            headers = {
                'Authorization': f'Bearer {token}',
                'Content-Type': 'application/json'
            }
            data = {
                "modelUri": f"gpt://{folder_id}/yandexgpt-lite",
                "completionOptions": {
                    "stream": False,
                    "temperature": 0.6,
                    "maxTokens": self.max_tokens

                },
                "messages": [
                    {
                        "role": "user",
                        "text": text + CONTINUE_STORY + user
                    }
                ]
            }
            response = requests.post("https://llm.api.cloud.yandex.net/foundationModels/v1/completion",
                                     headers=headers,
                                     json=data)

            if response.status_code == 200:
                text = response.json()["result"]["alternatives"][0]["message"]["text"]
                return text
            else:
                raise RuntimeError(
                    'Invalid response received: code: {}, message: {}'.format(
                        {response.status_code}, {response.text}
                    )
                )

        except Exception as e:
            error_gpt1 = error666
            logging.error(str(e))
            return error_gpt1
