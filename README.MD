# Using MongoDB with Django with CRUD (Create, Read, Update, Delete)

Requirements:

    * Django==2.2.14
    https://docs.djangoproject.com/en/2.2/
    
    * MongoDB v4.2.8
    https://docs.mongodb.com/manual/installation/
    * pymongo==3.10.1
    
Django 2.2 is a LTS, hence why I chose it.
https://www.djangoproject.com/download/
![Django Release Roadmap](https://github.com/jcamier/dfw_django_mongo_talk/blob/master/django_release_roadmap.png)    
![Django Release Dates](https://github.com/jcamier/dfw_django_mongo_talk/blob/master/django_release_dates.png)

Quick NoSQL terminology:
    A collection is similar to a table in SQL databases
    A document is a record

# Instructions:

## Step 1 Download and Install Dependencies
    Download and install MongoDB

    pip install -r requirements.txt
    
## Step 2 - Create user in MongoDB
    # Start mongo shell
    
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

## Step 3 - Create first app
    django-admin startproject mysite
    
    cd mysite/
    
    python manage.py runserver
    
    ctrl + c
    
    python manage.py startapp polls
    
    
## Step 4 Django
1. update mysite/mysite/settings.py file
    ```
    # Add POLLS_DIR
    POLLS_DIR = os.path.join(BASE_DIR, "polls", "templates", "polls")
    
    # Change your SECRET_KEY ...
    
    # Change your ALLOWED_HOSTS to your external IP address or use wildcard
    ALLOWED_HOSTS = ['*']
   
    # Modify templates section to include above POLLS_DIR   
    TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [POLLS_DIR],
    
    # We will not change the database settings since we will just change the
    functionality in how it works
   
    ```


2. modify mysite/polls/views.py:
    
    - copy and paste code from github repo

3. create mysite/polls/urls.py file:

    - copy and paste code from github repo

4. modify mysite/mysite/urls.py file (main directory):

    ```
    
    from django.contrib import admin
    from django.urls import include, path

    urlpatterns = [
    path('polls/', include('polls.urls')),
    path('admin/', admin.site.urls),
    ]
    
    ```

5. create mysite/polls/mongo_settings.py
    
    ```
   # Logging
    LOG_FORMAT = '%(asctime)s::%(name)s::%(funcName)s:%(lineno)d::%(levelname)s::%(message)s'
    LOG_LEVEL = "INFO"

    # MongoDB (Make sure you created the credentials above!!)
    MONGO_HOST = "localhost"
    MONGO_PORT = "27017"
    MONGO_USER = "django"
    MONGO_PASS = "PythonIsAwesome"
    DATABASE = "django"
    
    ```
      
6. create mysite/polls/mongo_session.py file 
    
    - copy and paste from repo

7. create templates directory and polls subdirectory

    - mysite/polls/templates/polls
    
8. copy and paste templates from repo
    - mysite/polls/templates/polls/index.html
    - mysite/polls/templates/polls/query_form.html
    - mysite/polls/templates/polls/simple_form.html
    - mysite/polls/templates/polls/update_form.html

9. create mysite/polls/urls.py file

    - copy and paste from repo
    
10. cd into directory mysite/

    - python manage.py runserver

11. Go to developement server url:

    http://127.0.0.1:8000/polls/
    
12. (C)reate a document (record)

    http://127.0.0.1:8000/polls/form
    
13. (R)ead - Query documents (records)

    http://127.0.0.1:8000/polls/query-form
    
13. (U)pdate documents (records)

    http://127.0.0.1:8000/polls/update-form
    
14. (D)elete documents (records)

    http://127.0.0.1:8000/polls/update-form
    
    



    