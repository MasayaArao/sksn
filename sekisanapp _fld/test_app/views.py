from django.shortcuts import render, redirect  # 追記
from .forms import FileUploadForm # 追記
from .models import FileUpload


def index(request):
    file_obj = FileUpload.objects.all()
    return render(request, 'test_app/index.html', {'file_obj': file_obj})

def new_file(request):

    if request.method == "POST":
        form = FileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('test_app:index')
    else:
        form = FileUploadForm()
    return render(request, 'test_app/new_file.html', {'form': form })