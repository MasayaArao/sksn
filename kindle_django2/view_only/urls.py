#path関数、Viewの読み込み
from django.urls import path
#from .import views
from .import views

#urlpatternsはアプリでリクエスト可能なパスを持つリスト
urlpatterns = [
    #viewonlyアプリで登録したルーティングをプロジェクトに反映
    path('',views.index),#1つ目の引数のパスでリクエストが届いたら、2つ目の引数の場所（view）で処理をする
    path('tokyo',views.tokyo),
    path('main',views.main),
    path('nagoya',views.nagoya),
]