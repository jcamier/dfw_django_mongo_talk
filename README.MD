# Using MongoDB with Django

Requirements:

    * Django==2.2.14
    https://docs.djangoproject.com/en/2.2/
    
    * MongoDB v4.2.8
    https://docs.mongodb.com/manual/installation/
    * pymongo==3.10.1

# Instructions:

## Step 1 - Install dependencies
    pip install -r requirements.txt
    
## Step 2 - Create user in MongoDB
    # Start mongo shell
    
    ```
    mongo
    use admin;
    
    db.createUser({
          user: "django",
          pwd: "PythonIsAwesome",
          roles: [
                    { role: "userAdminAnyDatabase", db: "admin" },
                    { role: "readWriteAnyDatabase", db: "admin" },
                    { role: "dbAdminAnyDatabase",   db: "admin" }
                 ]
    }); 
    ```

## Step 3 - Create first app
    django-admin startproject mysite
    cd mysite/
    python manage.py runserver
    ctrl + c
    python manage.py startapp polls
    
## Step 4 - create first view

1. modify mysite/polls/views.py:

    ```
    
    from django.http import HttpResponse
    
    def index(request):
        return HttpResponse("Hello, world. You're at the polls index.")
    
    ```

2. nano mysite/polls/urls.py file (create this file):

    ```
    
    from django.urls import path
    
    from . import views
    
    urlpatterns = [
        path('', views.index, name='index'),
    ]
    ```

3. modify mysite/urls.py file (parent directory):

    ```
    
    from django.contrib import admin
    from django.urls import include, path
    
    urlpatterns = [
        path('polls/', include('polls.urls')),
        path('admin/', admin.site.urls),
    ]
    
    ```

4. python manage.py runserver

5. http://127.0.0.1:8000/polls/

    ctrl + c

6. nano mysite/polls/mongo_settings.py

    ```
   # Logging
    LOG_FORMAT = '%(asctime)s::%(name)s::%(funcName)s:%(lineno)d::%(levelname)s::%(message)s'
    LOG_LEVEL = "INFO"

    # MongoDB (Make sure you created the credentials above)
    MONGO_HOST = "localhost"
    MONGO_PORT = "27017"
    MONGO_USER = "django"
    MONGO_PASS = "PythonIsAwesome"
    DATABASE = "django"
    
    ```
   
7. Update settings.py file
    ```
    ALLOWED_HOSTS = ['*']
    POLLS_DIR = os.path.join(BASE_DIR, "polls", "templates", "polls")
    TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [POLLS_DIR],
    etc...
    ```
  
   
7. copy mongo_session.py file from repo and save it in mysite/polls/mongo_session.py

8. create template directory in poll project
    - mysite/polls/templates
    
9. copy the templates from repo
    - mysite/polls/templates/simple_form.html

9. Add import statement to mysite/polls/views.py in order to access Mongo from Django
    ```
    from .mongo_session import DjangoMongoClient
    ```

    