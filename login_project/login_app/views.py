from django.shortcuts import render, redirect
from .form import SignupForm, LoginForm
from django.contrib.auth import login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

def signup_view(request):
    if request.method == 'POST':

        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()

    else:
        form = SignupForm()
    
    param = {
        'form': form
    }

    return render(request, 'login_app/signup.html', param)

def login_view(request):#ユーザーのログイン
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)

        if form.is_valid():
            user = form.get_user()

            if user:
                login(request, user)
                return redirect(to='/login_app/user/')

    else:
        form = LoginForm()

    param = {
        'title': 'ログイン',
        'form': form,
    }

    return render(request, 'login_app/login.html', param)

def logout_view(request):#ユーザーのログアウト
    logout(request)

    return render(request, 'login_app/logout.html')

@login_required
def user_view(request):#ログインユーザーの情報の表示
    user = request.user

    params = {
        'user': user
    }

    return render(request, 'login_app/user.html', params)

@login_required
def other_view(request):#他のユーザーの情報の表示
    users = User.objects.exclude(username=request.user.username)

    params = {
        'users': users
    }

    return render(request, 'login_app/other.html', params)