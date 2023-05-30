#HttpResponse（レスポンスを作るための関数）を読み込む
from django.http import HttpResponse

#indexメソッドの定義
def index(request):
    #レスポンスとして「Hello world!」という文字を返す
    return HttpResponse("積算データベース")

def tokyo(request):
    return HttpResponse("東京支店")

def main(request):
    return HttpResponse("本社")

def nagoya(request):
    return HttpResponse("名古屋支店")