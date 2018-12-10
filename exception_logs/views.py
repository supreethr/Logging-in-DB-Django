from rest_framework.exceptions import ValidationError

def exception_view(request):
    raise ValidationError('Custom error message...')
