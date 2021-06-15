from django.shortcuts import render, redirect, HttpResponse
from .forms import formRegister
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout as do_logout
from django.contrib.auth.models import User

# Create your views here.


def register(request):
    if request.method == 'POST':
        form = formRegister(request.POST)

        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.set_password(
                form.cleaned_data['password'])
            new_user.save()
            login(request, user=new_user)
            return redirect('Home')
    else:

        form = formRegister()

    return render(request, 'autenticacion/register.html', {'form': form})


def logout(request):

    do_logout(request)

    return redirect('Home')


def profile(request):

    user = User.objects.all()

    return render(request, 'registration/profile.html', {'user': user})
