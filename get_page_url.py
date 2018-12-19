import requests # Для запроса по URL

import config


def get_page_url(genre):
    params = {
        "search_query": genre,
        "sp": "CAMSAhgB" # Параметр отвечает за поиск по числу просмотров и длина видео меньше 4 минут
    }
    try:
        result = requests.get(config.YOUTUBE_DEFAULT_URL, params=params)
        result.raise_for_status() # Проверяем возвращает ли сервер HTTP 200
        return result.text
    except (requests.RequestException, ValueError): # Обрабатываем ошибки сети(requests) и ValueError проверяет reuests.raise_for_status()
        print("Произошла ошибка")
        return False
