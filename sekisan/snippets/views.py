from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse,HttpResponseForbidden
from .forms import FileUploadForm,FileUploadForm2 # 追記
from snippets.models import FileUpload,FileUpload2

from snippets.forms import SnippetForm, CommentForm,SearchForm,SnippetForm,SnippetForm2, CommentForm2,SearchForm2
from snippets.models import Snippet, Comment,Snippet2, Comment2
from django.db.models import Q

def index(request):
    return render(request, "snippets/index.html")

def top(request):
    snippets = Snippet.objects.all()
    context = {"snippets": snippets}

    form = SearchForm()
    query = None
    query2 = None
    query3 = None
    results = []
    if 'query'in request.GET:
        form = SearchForm(request.GET)

        if form.is_valid():
            query = form.cleaned_data['query']
            query2 = form.cleaned_data['query2']
            query3 = form.cleaned_data['query3']
            q = Q()
            if query:
                q &=  Q(title__icontains=query)|Q(code__icontains=query)
            if query2:
                q &= Q(language__icontains=query2)
                #results = Snippet.objects.filter(Q(title__icontains=query)|Q(code__icontains=query),Q(language__icontains=query2))
            if query3:
                q &= Q(status__icontains=query3)
            if not q:  # クエリがない場合は全てのSnippetを返す
                results = Snippet.objects.all()
            else:
                results = Snippet.objects.filter(q)

    return render(request, "snippets/top.html", {'form': form, 'query': query, 'query2': query2,'query3': query3,'results': results,'context':context,'snippets':snippets})

    #return render(request, "snippets/top.html", context)


@login_required
def snippet_new(request):
    if request.method == 'POST':
        form = SnippetForm(request.POST)
        if form.is_valid():
            snippet = form.save(commit=False)
            snippet.created_by = request.user
            snippet.save()
            messages.add_message(request, messages.SUCCESS,
                                 "ポイントを作成しました。")
            return redirect(snippet_detail, snippet_id=snippet.pk)
        else:
            messages.add_message(request, messages.ERROR,
                                 "ポイントの作成に失敗しました。")
    else:
        form = SnippetForm()
    return render(request, "snippets/snippet_new.html", {'form': form})


@login_required
def snippet_edit(request, snippet_id):
    snippet = get_object_or_404(Snippet, pk=snippet_id)
    if snippet.created_by_id != request.user.id:
        return HttpResponseForbidden("このポイントの編集は許可されていません。")

    if request.method == "POST":
        form = SnippetForm(request.POST, instance=snippet)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS,
                                 "ポイントを更新しました。")
            return redirect('snippet_detail', snippet_id=snippet_id)
        else:
            messages.add_message(request, messages.ERROR,
                                 "ポイントの更新に失敗しました。")
    else:
        form = SnippetForm(instance=snippet)
    return render(request, 'snippets/snippet_edit.html', {'form': form})


@login_required
def snippet_detail(request, snippet_id):
    snippet = get_object_or_404(Snippet, pk=snippet_id)
    comments = Comment.objects.filter(commented_to=snippet_id).all()
    comment_form = CommentForm()
    #page_n = '/' + str(snippet_id) + '/'
    page_n = str(snippet_id)
    file_obj = FileUpload.objects.filter(upload__contains ='/%s/' % page_n).all()
    #file_obj = FileUpload.objects.filter(upload__contains = '/2/').all()
    #file_obj = FileUpload.objects.filter(id = snippet_id).all()
    fu_Form = FileUploadForm()
    #file_obj = FileUpload.objects.all()
    
    duedate = Snippet.duedate
    

    return render(request, "snippets/snippet_detail.html", {
        'snippet': snippet,
        'comments': comments,
        'comment_form': comment_form,
        'fu_form':fu_Form,
        'file_obj': file_obj,
        ##'FileUploads': FileUploads,
        ##'FileUpload_Form': FileUpload_Form,
    })


@login_required
def comment_new(request, snippet_id):
    snippet = get_object_or_404(Snippet, pk=snippet_id)

    form = CommentForm(request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.commented_to = snippet
        comment.commented_by = request.user
        comment.save()
        messages.add_message(request, messages.SUCCESS,
                             "コメントを投稿しました。")
    else:
        messages.add_message(request, messages.ERROR,
                             "コメントの投稿に失敗しました。")
    return redirect('snippet_detail', snippet_id=snippet_id)

@login_required
def new_file(request,snippet_id):
    #file_obj = FileUpload.objects.filter(pk=snippet_id)
    snippet = get_object_or_404(Snippet, pk=snippet_id)###
    if request.method == "POST":
        form = FileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            file = form.save(commit=False)
            file.id = snippet_id###
            file.page = snippet_id
            file.save()
            return redirect('snippet_detail', snippet_id=snippet_id)
    else:
        form = FileUploadForm()
    #context = {'file_obj': file_obj, 'form': form}
    #return render(request, 'snippet_detail', context)
    return redirect('snippet_detail', snippet_id=snippet_id)

def top2(request):
    snippets = Snippet2.objects.all()
    context = {"snippets": snippets}

    form = SearchForm2()
    query = None
    results = []
    if 'query' in request.GET:
        form = SearchForm2(request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']
            results = Snippet2.objects.filter(Q(title__icontains=query)|Q(code__icontains=query))
    return render(request, "snippets/top2.html", {'form': form, 'query': query, 'results': results,'context':context,'snippets':snippets})

@login_required
def snippet_new2(request):
    if request.method == 'POST':
        form = SnippetForm2(request.POST)
        if form.is_valid():
            snippet = form.save(commit=False)
            snippet.created_by = request.user
            snippet.save()
            messages.add_message(request, messages.SUCCESS,
                                 "ポイントを作成しました。")
            return redirect('snippet_detail2', snippet_id=snippet.pk)
        else:
            messages.add_message(request, messages.ERROR,
                                 "ポイントの作成に失敗しました。")
    else:
        form = SnippetForm2()
    return render(request, "snippets/snippet_new2.html", {'form': form})

@login_required
def snippet_edit2(request, snippet_id):
    snippet = get_object_or_404(Snippet2, pk=snippet_id)
    if snippet.created_by_id != request.user.id:
        return HttpResponseForbidden("このポイントの編集は許可されていません。")

    if request.method == "POST":
        form = SnippetForm2(request.POST, instance=snippet)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS,
                                 "ポイントを更新しました。")
            return redirect('snippet_detail2', snippet_id=snippet_id)
        else:
            messages.add_message(request, messages.ERROR,
                                 "ポイントの更新に失敗しました。")
    else:
        form = SnippetForm2(instance=snippet)
    return render(request, 'snippets/snippet_edit2.html', {'form': form})


@login_required
def snippet_detail2(request, snippet_id):
    snippet = get_object_or_404(Snippet2, pk=snippet_id)
    comments = Comment2.objects.filter(commented_to=snippet_id).all()
    comment_form = CommentForm2()
    #page_n = '/' + str(snippet_id) + '/'
    page_n = str(snippet_id)
    file_obj = FileUpload2.objects.filter(upload__contains ='/%s/' % page_n).all()
    #file_obj = FileUpload.objects.filter(upload__contains = '/2/').all()
    #file_obj = FileUpload.objects.filter(id = snippet_id).all()
    fu_Form = FileUploadForm2()
    #file_obj = FileUpload.objects.all()
    


    return render(request, "snippets/snippet_detail2.html", {
        'snippet': snippet,
        'comments': comments,
        'comment_form': comment_form,
        'fu_form':fu_Form,
        'file_obj': file_obj,
        ##'FileUploads': FileUploads,
        ##'FileUpload_Form': FileUpload_Form,
    })


@login_required
def comment_new2(request, snippet_id):
    snippet = get_object_or_404(Snippet2, pk=snippet_id)

    form = CommentForm2(request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.commented_to = snippet
        comment.commented_by = request.user
        comment.save()
        messages.add_message(request, messages.SUCCESS,
                             "コメントを投稿しました。")
    else:
        messages.add_message(request, messages.ERROR,
                             "コメントの投稿に失敗しました。")
    return redirect('snippet_detail2', snippet_id=snippet_id)

@login_required
def new_file2(request,snippet_id):
    #file_obj = FileUpload.objects.filter(pk=snippet_id)
    snippet = get_object_or_404(Snippet2, pk=snippet_id)###
    if request.method == "POST":
        form = FileUploadForm2(request.POST, request.FILES)
        if form.is_valid():
            file = form.save(commit=False)
            file.id = snippet_id###
            file.page = snippet_id
            file.save()
            return redirect('snippet_detail2', snippet_id=snippet_id)
    else:
        form = FileUploadForm2()
    #context = {'file_obj': file_obj, 'form': form}
    #return render(request, 'snippet_detail', context)
    return redirect('snippet_detail2', snippet_id=snippet_id)