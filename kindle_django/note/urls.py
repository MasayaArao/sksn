from django.urls import path
from.import views

urlpatterns = [
    path('', views.index, name="note_list"),
    path('<int:pk>', views.show, name="note_detail"),
    path('create', views.create, name="note_create"),
    path('params/<str:name>',views.show,name="mypage"),
    path('create',views.create,name='create'),
]
