from django.urls import path
from django.conf.urls import url

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    url(r'^form', views.insert_form_data, name='insert_form_data'),
    url(r'^query-form', views.query_form_data, name='query_form_data'),
    url(r'^update-form', views.update_delete_form_data, name='update_delete_form_data'),
]