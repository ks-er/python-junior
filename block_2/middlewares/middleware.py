import json
import time

from django.http import HttpResponse
from django.http import JsonResponse

from django.utils.deprecation import (
    MiddlewareMixin,
)

import sys


class StatisticMiddleware(MiddlewareMixin):
    """
    Компонент вычисляющий время выполнения запроса на сервере и размер ответа в байтах.
    Отображает значения в консоли приложения
    """
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        time_start = time.monotonic()
        response = self.get_response(request)
        time_end = time.monotonic()
        print(f'time response = {time_end - time_start}')
        print(len(response.content))
        return response


class FormatterMiddleware(MiddlewareMixin):
    """
    Компонент форматирующий Json ответ в HttpResponse
    {'key': value} => <p>key = value</p>
    """
    def process_response(self, request, response):
        try:
            decode_content = response.content.decode()
            data = json.loads(decode_content)

            new_data = list()
            for item in data.items():
                new_data.append(f'<p>{item[0]} = {item[1]}</p>')

            return HttpResponse(new_data)

        except:
            return response


class CheckErrorMiddleware(MiddlewareMixin):
    """
        Перехватывает необработанное исключение в представлении и отображает ошибку в виде
        "Ошибка: {exception}"
    """
    def process_exception(self, request, exception):
        return HttpResponse(f"Ошибка: {exception}")



