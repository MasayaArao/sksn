from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse,HttpResponseForbidden
from .forms import FileUploadForm # 追記
from snippets.models import FileUpload

from snippets.forms import SnippetForm, CommentForm
from snippets.models import Snippet, Comment


def top(request):
    snippets = Snippet.objects.all()
    context = {"snippets": snippets}
    return render(request, "snippets/top.html", context)


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
    ##FileUploads = FileUpload.objects.filter(uploaded_to=snippet_id).all()
    ##FileUpload_Form = FileUploadForm()
    file_obj = FileUpload.objects.all()

    return render(request, "snippets/snippet_detail.html", {
        'snippet': snippet,
        'comments': comments,
        'comment_form': comment_form,
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
def new_file(request):
    #snippet = get_object_or_404(Snippet, pk=snippet_id)
    form = FileUploadForm(request.POST, request.FILES)
    if form.is_valid():
        #FileUpload = form.save(commit=False)
        #FileUpload.uploaded_page = snippet
        #FileUpload.uploaded_by = request.user
        form.save()
        return redirect('top')
    return render( request,'snippets/new_file.html', {'form': form })
    #return render(request, 'snippets/new_file.html', {'form': form })
