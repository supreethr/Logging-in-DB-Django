from django.db import connection
from django.http import JsonResponse

class ExceptionMiddleware(object):
    def process_exception(self, request, exception):
        name = type(exception).__name__
        message = str(exception)
        response_data = {'name': name, 'error': message}
        return JsonResponse(response_data, status=200)
