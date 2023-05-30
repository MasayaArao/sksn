from django.urls import path
from .import views
urlpatterns = [
    path('',views.index),
    path('kara_age',views.karaage),
    path('sekisan',views.sekisan),
    path('apple',views.many_apple),
    path('banana/<int:num>',views.many_banana),
    path('product/<int:num1>/<int:num2>',views.product),
    #ex)gyomu?count=10
    path('gyomu',views.many_gyomu),
]
