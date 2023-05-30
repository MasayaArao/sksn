from django.shortcuts import render

def index(request):
    return render(request,"with_template/index.html",{})

def show(request,name):
    return render(request,"with_template/show.html",{'user_name':name})

def list(request):
    numbers = [1,2,3,4,5]
    return render(request,"with_template/list.html",{'numbers':numbers})
