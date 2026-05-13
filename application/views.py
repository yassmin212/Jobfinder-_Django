from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


def signup_view(request):

    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        if User.objects.filter(username=username).exists():
            return render(request, 'application/signup.html', {
                'error': 'Username already exists'
            })

        user = User.objects.create_user(
            username=username,
            email=email,
            password=password
        )

        login(request, user)
        return redirect('/') 

    return render(request, 'application/signup.html')


def login_view(request):

    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:
            login(request, user)

            
            if user.is_superuser:
                return redirect('admin_dashboard')
            else:
                return redirect('/')

        else:
            return render(request, 'application/login.html', {
                'error': 'Invalid username or password'
            })

    return render(request, 'application/login.html')


def logout_view(request):
    logout(request)
    return redirect('/')


@login_required
def admin_dashboard(request):

    if not request.user.is_superuser:
        return redirect('login')   

    
    users_count = User.objects.count()

    return render(request, 'application/admin-dashboard.html', {
        'users_count': users_count
    })