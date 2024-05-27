from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import redirect, render
from django.contrib import auth
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from traitlets import Instance
from django.contrib.auth.forms import PasswordResetForm


from cart.models import Cart
from users.forms import ProfileForm, UserLoginForm, UserRegistrationForm


def login(request):
    # Метод из документации обработки с кнопкой войти
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)

            session_key = request.session.session_key

            if user:
                auth.login(request, user)

                if session_key:
                    Cart.objects.filter(session_key=session_key).update(user=user)

                return HttpResponseRedirect(reverse('main:index'))
    else:
        form = UserLoginForm()

    context = {
        'title': 'aboba',
        'form': form
    }
    return render(request, 'users/login.html', context)


def registration(request):
    if request.method == 'POST':
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()

            session_key = request.session.session_key

            user = form.instance
            auth.login(request, user)

            if session_key:
                Cart.objects.filter(session_key=session_key).update(user=user)

            return HttpResponseRedirect(reverse('main:index'))
    else:
        form = UserRegistrationForm()

    context = {
        'title': 'aboba',
        'form': form
    }
    return render(request, 'users/registration.html', context)


@login_required
def profile(request):
    if request.method == 'POST':
        form = ProfileForm(data=request.POST, instance=request.user, files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('user:profile'))
    else:
        form = ProfileForm(instance=request.user)

    context = {
        'title': 'aboba',
        'form': form,
    }
    return render(request, 'users/profile.html', context)


@login_required
def logout(request):
    auth.logout(request)
    return redirect(reverse('main:index'))


def profile_design(request):
    """
    Контроллер, отвечающий за страницу "о нас" (about_page.html),
    та в свою очередь подгружает стили
    из папки styles_for_about_page
    """
    context = {

    }
    return render(request, 'users/profile_new.html', context=context)

def lost_pass(request):
    if request.method == 'POST':
        form = PasswordResetForm(data=request.POST)
        if form.is_valid():
            response_data = {'message': 'Письмо отправлено'}
            return JsonResponse(response_data)
    else:
        form = PasswordResetForm()

    context = {
        'title': 'aboba',
        'form': form,
    }
    return render(request, 'users/lost_pass.html', context)
