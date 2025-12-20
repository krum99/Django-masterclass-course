from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages


# Create your views here.

def register(request):
  form = UserCreationForm(request.POST or None)
  if request.method == "POST":
    if form.is_valid():
      username = form.cleaned_data.get('username')
      messages.success(request, f'Welcome {username}, your account has been successfully created')
      form.save()
      return redirect('myapp:index')

  
  return  render(request, 'users/register.html', {'form': form})
