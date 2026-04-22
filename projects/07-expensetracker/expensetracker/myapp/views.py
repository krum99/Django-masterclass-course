from django.shortcuts import render, redirect
from .forms import ExpenseForm
from .models import Expense
from django.db.models import Sum
import datetime


def get_expense_summary():
    total_expenses = Expense.objects.aggregate(Sum("amount"))["amount__sum"]

    # Logic to calculate 365 days expenses
    last_year = datetime.date.today() - datetime.timedelta(days=365)
    data = Expense.objects.filter(date__gt=last_year)
    yearly_sum = data.aggregate(Sum("amount"))["amount__sum"]

    # Monthly sum
    last_month = datetime.date.today() - datetime.timedelta(days=30)
    data = Expense.objects.filter(date__gt=last_month)
    monthly_sum = data.aggregate(Sum("amount"))["amount__sum"]
    # Weekly sum
    last_week = datetime.date.today() - datetime.timedelta(days=7)
    data = Expense.objects.filter(date__gt=last_week)
    weekly_sum = data.aggregate(Sum("amount"))["amount__sum"]

    # Calculating daily sum
    daily_sums = (
        Expense.objects.filter()
        .values("date")
        .order_by("date")
        .annotate(sum=Sum("amount"))
    )

    return {
        "total_expenses": total_expenses,
        "yearly_sum": yearly_sum,
        "monthly_sum": monthly_sum,
        "weekly_sum": weekly_sum,
        "daily_sums": daily_sums,
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

    context = {"expense_form": expense_form, "expenses": expenses, **summary}

    return render(request, "myapp/index.html", context)


def edit(request, id):
    expense = Expense.objects.get(id=id)
    expense_form = ExpenseForm(instance=expense)
    if request.method == "POST":
        form = ExpenseForm(request.POST, instance=expense)
        if form.is_valid():
            form.save()
            return redirect("index")
    return render(request, "myapp/edit.html", {"expense_form": expense_form})


def delete(request, id):
    if request.method == "POST":
        expense = Expense.objects.get(id=id)
        expense.delete()
    return redirect("index")
