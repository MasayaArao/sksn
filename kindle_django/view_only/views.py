from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello world!")

def karaage(request):
    return HttpResponse("唐揚げ"*5)

def sekisan(request):
    return HttpResponse("積算"*2)

def many_apple(request):
    count = int(request.GET['count'])
    return HttpResponse("Apple,"*count)

def many_banana(request,num):
    return HttpResponse("Banana,"*num)

def product(request,num1,num2):
    return HttpResponse("<h1>%d × %d = %d</h1>"%(num1,num2,num1*num2))

def many_gyomu(request):
    count = int(request.GET['count'])
    return HttpResponse("業務,"*count)

def many_gyomu(request):
    count = int(request.GET['count'])
    return HttpResponse("業務,"*count)


