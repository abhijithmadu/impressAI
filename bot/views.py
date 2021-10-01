from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from .models import UserCount
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.conf import settings
import telegram


URL = settings.BOT_URL
bot_token = settings.BOT_TOKEN
bot_chat_id = settings.BOT_CHAT_ID

def telegram_bot(request, message, bot_chat_id=bot_chat_id, token=bot_token):
    bot = telegram.Bot(token=token)
    bot.sendMessage(chat_id=bot_chat_id, text=message)

@login_required(login_url='login')
def home(request):
    user_count = UserCount.objects.all()
    return render(request,'home.html',{'user_count':user_count})    

def login(request):
    if request.method == 'GET':
        return render(request,'login.html')   

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            usr = User.objects.get(username=username, password=password)
            auth_login(request, usr)
            return redirect('home')
        except User.DoesNotExist:
            error = 'Invalid creditials ! !'
            return render(request, 'login.html', {'error':error})

def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html')

    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password_confirmation = request.POST.get('confirm_password')
        if password == password_confirmation:
            print("user succesfully created")
            user = User.objects.create(username=username, email=email, password=password)
            auth_login(request, user)
            return redirect('home')
        else:
            pwrd_error = "password did not match"
            return render(request, 'signup.html', {'pword_error': pwrd_error})

    return render(request, 'signup.html')


def logout(request):
    auth_logout(request)
    return redirect('login')


def stupid(request):
    telegram_bot(request, "Stupid")

    user = request.user
    if UserCount.objects.filter(user=user).exists():
        user_count = UserCount.objects.get(user=user)
    else:
        user_count = UserCount.objects.create(user=user)

    user_count.stupid += 1
    user_count.save()

    return redirect('home')

def fat(request):
    telegram_bot(request, "Fat")

    user = request.user
    if UserCount.objects.filter(user=user).exists():
        user_count = UserCount.objects.get(user=user)
    else:
        user_count = UserCount.objects.create(user=user)

    user_count.fat += 1
    user_count.save()

    return redirect('home')

def dumb(request):
    telegram_bot(request, "Dumb")

    user = request.user
    if UserCount.objects.filter(user=user).exists():
        user_count = UserCount.objects.get(user=user)
    else:
        user_count = UserCount.objects.create(user=user)

    user_count.dumb += 1
    user_count.save()

    return redirect('home')
