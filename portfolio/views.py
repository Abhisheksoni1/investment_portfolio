import json

from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required

from django.contrib.auth import login, authenticate, logout
from django.http import HttpResponse

from portfolio.forms import UserCreationForm
from django.shortcuts import render
from portfolio.forms import LoginForm
from django.shortcuts import redirect

from portfolio.models import Client, Fund, Portfolio


@staff_member_required
def admin_bar(request, id=None):
    try:
        if not id:
            portfolio = Portfolio.objects.all()[0]
            funds = Fund.objects.filter(user=request.user, portfolio=portfolio)
        else:
            funds = Fund.objects.get(user=request.user, portfolio__id=id)

        dates = list(map(lambda i: i.date.strftime('%m-%d-%Y'), funds))
        net_nav = list(map(lambda i: float(i.net_nav), funds))
        item = {'dates': dates,
                'net_nav': net_nav}
        return HttpResponse(json.dumps(item), content_type='application/json')

    except Exception as e:
        return HttpResponse(json.dumps({'error': 404}), content_type='application/json')


def bar(request, id=None):
    if request.user.is_authenticated:
        try:
            if id is None:
                client = Client.objects.filter(user=request.user)[0]
            else:
                client = Client.objects.get(user=request.user, portfolio__id=id)

            data = Fund.objects.filter(user=client.investor, portfolio=client.portfolio)
            dates = list(map(lambda i: i.date.strftime('%m-%d-%Y'), data))
            net_nav = list(map(lambda i: (float(client.shares)*float(i.net_nav))/100, data))
            item = {'dates': dates,
                    'net_nav': net_nav}
            return HttpResponse(json.dumps(item), content_type='application/json')
        except Exception as e:
            print(e)
            return HttpResponse(json.dumps({'error': 404}), content_type='application/json')
    else:
        return HttpResponse(json.dumps({'error': 'not authorise'}), content_type='application/json')


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
        else:
            msg = 'Please check your details!'

            if 'username' in form.errors:
                msg = 'username already exist'

            if 'password2' in form.errors:
                msg = 'Password didn\'t match'

            return render(request, 'signup.html', {'registerErrorMsg': msg,
                                                   'form': form})
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})


@login_required
def home(request):
    data = Client.objects.filter(user=request.user)
    portfolio = map(lambda i: i.portfolio, data)
    # print(portfolio)
    return render(request, 'home.html', {'portfolios': portfolio})


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'login.html', {'loginErrorMsg': 'username password not match',
                                                  'form': form})
    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form})


def logout_view(request):
    logout(request)
    return render(request, 'logout.html')
