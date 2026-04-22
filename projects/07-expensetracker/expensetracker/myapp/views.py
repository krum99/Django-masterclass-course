from django.shortcuts import render
from .forms import ExpenseForm

# Create your views here.


def index(request):
  if request.method == "POST":
    expense_form = ExpenseForm(request.POST)
    if expense_form.is_valid():
      expense_form.save()
  else:
    expense_form = ExpenseForm()
  
  return render(request, 'myapp/index.html', {'expense_form': expense_form})