from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.core.paginator import Paginator
from django.views.decorators.cache import cache_page

from .models import Item
from .forms import ItemForm
# Create your views here.

# @cache_page(60 * 15)
@login_required
def index(request):
  item_list = Item.objects. all()
  paginator = Paginator(item_list, 5)
  page_number = request.GET.get("page")
  page_obj = paginator.get_page(page_number)

  context = {
    'page_obj': page_obj,
  }
  return  render(request, "myapp/index.html", context)


class IndexClassView(ListView):
  model = Item
  template_name = "myapp/index.html"
  context_object_name = 'item_list'

# def detail (request, id):
#   item = Item.objects.get(id=id)
#   context = {
#     'item': item
#   }
#   return render(request, 'myapp/detail.html', context)

class FoodDetail(DetailView):
  model = Item
  template_name = 'myapp/detail.html'
  context_object_name = 'item'

def create_item(request):
  form = ItemForm(request.POST or None)
  if request.method == 'POST':
    if form.is_valid():
      form.save()
      return redirect('myapp:index')

  context={
    'form': form
  }
  return render(request, 'myapp/item-form.html', context)

class ItemCreateView(CreateView):
  model = Item
  fields = ['item_name', 'item_desc', 'item_price', 'item_image']

  def form_valid(self, form):
    form.instance.user_name = self.request.user
    return super().form_valid(form)


def update_item(request, id):
  item = Item.objects.get(id=id)
  form=ItemForm(request.POST or None, instance=item)

  if form.is_valid():
    form.save()
    return redirect('myapp:index')

  context = {
    'form': form
  }
  return render(request, 'myapp/item-form.html', context)

class ItemUpdateView(UpdateView):
  model = Item
  fields = ['item_name', 'item_desc', 'item_price', 'item_image']
  template_name_suffix = '_update_form'

def delete_item(request, id):
  item = Item.objects.get(id=id)
  if request.method == 'POST':
    item.delete()
    return redirect('myapp:index')
      
  return render(request, 'myapp/item-delete.html')

class ItemDeleteView(DeleteView):
  model = Item
  success_url = reverse_lazy('myapp:index')


# def get_objects(request):
#   for item in Item.objects.all():
#     print(item.item_name)

# def get_objects_optimized(request):
#   items = Item.objects.only('item_name')

#   for item in items:
#     print(item.item_name)
