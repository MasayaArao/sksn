from django.urls import path

from hello import views

urlpatterns = [
    path('upload', views.model_form_upload, name='upload')
]