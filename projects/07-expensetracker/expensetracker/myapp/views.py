from django.shortcuts import render, redirect
from .forms import ExpenseForm
from .models import Expense

# Create your views here.


def index(request):
  if request.method == "POST":
    expense_form = ExpenseForm(request.POST)
    if expense_form.is_valid():
      expense_form.save()
  else:
    expense_form = ExpenseForm()
  
  return render(request, 'myapp/index.html', {'expense_form': expense_form})

def edit(request, id):
  expense = Expense.objects.get(id=id)
  expense_form = ExpenseForm(instance=expense)
  if request.method == "POST":
    form = ExpenseForm(request.POST,instance=expense)
    if form.is_valid():
      form.save()
      return redirect('index')
  return render(request, 'myapp/edit.html', {'expense_form': expense_form})
