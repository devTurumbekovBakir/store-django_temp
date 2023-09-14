from django.shortcuts import render, HttpResponseRedirect, reverse
from django.contrib import auth, messages
from .forms import UserLoginForm, UserRegistrationForm, UserProfileForm

from products.models import Basket

from django.contrib.auth.decorators import login_required


def login(request):
    """
    Обработчик страницы входа в систему.
    Args:
        request (HttpRequest): Запрос от клиента.
    Returns:
        HttpResponse: Ответ сервера, содержащий страницу входа или перенаправление на главную.
    """
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('index'))
    else:
        form = UserLoginForm()
    context = {'form': form}
    return render(request, 'users/login.html', context)


def registration(request):
    """
    Обработчик страницы регистрации нового пользователя.
    Args:
        request (HttpRequest): Запрос от клиента.
    Returns:
        HttpResponse: Ответ сервера, содержащий страницу регистрации или перенаправление на страницу входа.
    """
    if request.method == 'POST':
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Вы успешно зарегистрированы!')
            return HttpResponseRedirect(reverse('login'))
    else:
        form = UserRegistrationForm()
    context = {'form': form}
    return render(request, 'users/registration.html', context)


@login_required
def profile(request):
    """
    Обработчик страницы профиля пользователя.
    Args:
        request (HttpRequest): Запрос от клиента.
    Returns:
        HttpResponse: Ответ сервера, содержащий страницу профиля или обработку изменений профиля.
    """
    if request.method == 'POST':
        form = UserProfileForm(instance=request.user, data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Вы успешно обновили профиль!')
            return HttpResponseRedirect(reverse('profile'))
        else:
            print(form.errors)
    else:
        form = UserProfileForm(instance=request.user)

    baskets = Basket.objects.filter(user=request.user)

    context = {
        'title': 'Store - Профиль',
        'form': form,
        'baskets': Basket.objects.filter(user=request.user),
    }
    return render(request, 'users/profile.html', context)


def logout(request):
    """
    Обработчик выхода пользователя из системы.
    Args:
        request (HttpRequest): Запрос от клиента.
    Returns:
        HttpResponse: Ответ сервера с перенаправлением на главную страницу.
    """
    auth.logout(request)
    return HttpResponseRedirect(reverse('index'))
