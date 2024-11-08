# myapp/views.py
# from django.http import HttpResponse
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods


@require_http_methods(["GET"])
def get_response(request):
    data = {
        'name': "Salman",
        'age': 30,
        'address': "123 Main St, City, State, Zip"
    }

    return JsonResponse(data)
