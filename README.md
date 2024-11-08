# Django-practice

GET Request View Using JsonResponse
In your myapp/views.py, define the get_data view to handle a GET request and respond with JSON data:

python
Copy code

# myapp/views.py

```
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods

@require_http_methods(["GET"])
def get_data(request):
    # Sample data to return as JSON
    data = {
        "message": "This is a response to a GET request.",
        "status": "success",
        "items": ["item1", "item2", "item3"]
    }

    # Return the data as a JSON response
    return JsonResponse(data)
```

Explanation of the Code
@require_http_methods(["GET"]): This decorator restricts the view to only accept GET requests. If another HTTP method is used, it automatically responds with a 405 (Method Not Allowed) error.
data dictionary: This sample dictionary contains data that will be serialized into JSON format.
JsonResponse(data): Converts the data dictionary into JSON and returns it with the Content-Type header set to application/json.
URL Configuration
In myapp/urls.py, map this view to a URL:

# myapp/urls.py

```from django.urls import path
from . import views

urlpatterns = [
    path('get-data/', views.get_data, name='get_data'),
]

```

Testing the GET Request
Start the server:

bash
Copy code
python manage.py runserver
Access the JSON response by visiting http://127.0.0.1:8000/myapp/get-data/ in your browser or using curl:

bash
Copy code
curl http://127.0.0.1:8000/myapp/get-data/
The JSON response should look like this:

json
Copy code
{
"message": "This is a response to a GET request.",
"status": "success",
"items": ["item1", "item2", "item3"]
}
This example ensures the response data is returned in JSON format, making it suitable for APIs or applications that consume JSON data.
