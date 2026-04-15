from django.shortcuts import render, redirect
from .models import Food, Consume
# Create your views here.

def index(request):
    if request.method=="POST":
        #GEtting the id of item selected from our front-end
        consumed_food_id = request.POST['food']
        #Passing the id and getting the actual food item from our model
        food = Food.objects.get(id=consumed_food_id)
        # Getting the logged in user from request objecy
        user = request.user
        # Creating the consume object, consuming food
        consume = Consume(user=user,food_consumed=food)
        consume.save()

    foods = Food.objects.all()
    consumed_food = Consume.objects.filter(user=request.user)

    return render(request,'myapp/modern-index.html',{'foods':foods,'consumed_food':consumed_food})

def delete_consume(request,id):
    if request.method=="POST":
        consumed_food = Consume.objects.get(id=id)
        consumed_food.delete()
        return redirect("/")
    return render(request,'myapp/delete.html')