from django.urls import path
from . import views

app_name = 'test_app'

urlpatterns = [
        path('', views.index, name='index'),
        path('new_file', views.new_file, name='new_file'),  # 追加
]