# Em thesimplewayofsaving_app/allfinance/views.py

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from .forms import BudgetForm
from .models import Budget


def index(request):
    return render(request, 'allfinance/index.html')


def create_budget(request):
    if request.method == 'POST':
        form = BudgetForm(request.POST)
        if form.is_valid():
            budget = form.save(commit=False)
            budget.user = request.user
            budget.save()
            return redirect('allfinance/list_budgets')
    else:
        form = BudgetForm()
    return render(request, 'allfinance/create_budget.html', {'form': form})

def list_budgets(request):
    budgets = Budget.objects.filter(user=request.user)
    return render(request, 'allfinance/list_budgets.html', {'budgets': budgets})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('list_budgets')  # Redireciona para a lista de orçamentos após o login
    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})
