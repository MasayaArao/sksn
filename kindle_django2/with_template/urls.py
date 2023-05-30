from django.urls import path
from .import views

urlpatterns = [
    #viewonlyアプリで登録したルーティングをプロジェクトに反映
    path('',views.index,name="index"),#1つ目の引数のパスでリクエストが届いたら、2つ目の引数の場所（view）で処理をする
    path('params/<str:name>',views.show,name="mypage"),
    path('list',views.list,name="list"),
]