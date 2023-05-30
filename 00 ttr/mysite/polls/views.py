from django.http import HttpResponse, Http404 #追加
from django.shortcuts import get_object_or_404, render

from django.http import HttpResponse

from django.template import loader

from .models import Question
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # Question を order_by(-pub_date) でソートし、前から5つの配列を取得
    #   マイナスをつけるだけでデータを降順にしてくれる。
    #   [:5] は配列をスライスする。[0:5]と同じで0番目から5つ取得する意味。
    # テンプレートの読み込み
    template = loader.get_template('polls/index.html')

    # テンプレートで使う変数を設定
    context = {
        'latest_question_list': latest_question_list,
    }
    return render(request, 'polls/index.html', context)

#def index(request):
    #return HttpResponse("Hello, world. You're at the polls index.")

def detail(request, question_id):
    '''
    try:
        question = Question.objects.get(pk=question_id)
        # 主キーはそのカラム名に関わらず pk= で検索できる
    except Question.DoseNotExist:
        raise Http404('Question does not exist')
    return render(request, 'polls/detail.html', {'question': question})
    '''
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)