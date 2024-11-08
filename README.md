> 8<sup>th</sup> Nov 2024
# Django API Tutorial: Handling GET and POST Requests with JSON Responses
#### This tutorial will guide you through creating a basic Django project with an app that includes endpoints to handle GET and POST requests and returns JSON responses. This setup can be used for simple APIs or as a foundation for more complex applications.

### Prerequisites:
- Python and Django installed on your machine.
- Familiarity with basic Django concepts (apps, views, and URLs).

###  Step 1: Set Up Your Django Project
---
Create a new Django project:
```python
django-admin startproject myproject
cd myproject
```
Start a new Django app:
```python
python manage.py startapp myapp
Use code with caution.
```
Register the app in your project settings. Open myproject/settings.py and add 'myapp' to the INSTALLED_APPS list:
```python
INSTALLED_APPS = [
    ...
    'myapp',
]
```

### Step 2: Create URL Configurations
---
We'll set up URLs in both the project-level urls.py and the app-level urls.py to organize our routes.
```python
Project-level urls.py:
```
In `myproject/urls.py,` include the app's URL configurations:
```python
# myproject/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('myapp/', include('myapp.urls')),  # Include myapp's URLs
]
```

App-level `urls.py`:

In `myapp/urls.py` (create the file if it doesn't exist), define URL patterns for GET and POST endpoints:

```Python
# myapp/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('get-data/', views.get_data, name='get_data'),  # GET endpoint
    path('post-data/', views.post_data, name='post_data'),  # POST endpoint
]
```

### Step 3: Create Views to Handle GET and POST Requests
---
Now, we'll create two views in myapp/views.py: one for handling GET requests and another for POST requests.

`GET` Request View with JSON Response

In `myapp/views.py`, define a view `function get_data` to handle GET requests and respond with JSON data.

```Python
# myapp/views.py
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods

@require_http_methods(["GET"])
def get_data(request):   

    data = {
        "message": "This is a response to a GET request.",
        "status": "success",
        "items": ["item1", "item2", "item3"]
    }
    return JsonResponse(data)
```
> To get the api data: `http://127.0.0.1:8000/myapp/get-data/`
