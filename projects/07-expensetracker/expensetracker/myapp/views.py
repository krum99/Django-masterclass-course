from django.shortcuts import render, redirect
from .forms import ExpenseForm
from .models import Expense
from django.db.models import Sum

def get_expense_summary():
   total_expenses = Expense.objects.aggregate(Sum("amount"))['amount__sum']

   return {
      'total_expenses': total_expenses,
   }

def index(request):
  if request.method == "POST":
    expense_form = ExpenseForm(request.POST)
    if expense_form.is_valid():
      expense_form.save()
  else:
    expense_form = ExpenseForm()
    
  expenses = Expense.objects.all()
  summary = get_expense_summary()

  context = {
    'expense_form': expense_form,
    'expenses': expenses,
    **summary
    }

  return render(request, 'myapp/index.html', context)

def edit(request, id):
  expense = Expense.objects.get(id=id)
  expense_form = ExpenseForm(instance=expense)
  if request.method == "POST":
    form = ExpenseForm(request.POST,instance=expense)
    if form.is_valid():
      form.save()
      return redirect('index')
  return render(request, 'myapp/edit.html', {'expense_form': expense_form})

def delete(request, id):
    if request.method=="POST":
        expense = Expense.objects.get(id=id)
        expense.delete()
    return redirect('index')