from django.shortcuts import render,redirect
from .forms import DocumentForm
from .models import Document

def model_form_upload(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            #return redirect('index')
            return redirect('upload')
    else:
        form = DocumentForm()
        obj = Document.objects.all()
    return render(request, 'hello/model_form_upload.html', {
        'form': form,
        'obj': obj
    })