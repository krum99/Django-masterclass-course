from django.shortcuts import render
from django.http import HttpResponse

from .forms import CreateUserForm

def register(request):
  form = CreateUserForm()
  return render(request, 'users/register.html', {'form': form})
