from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Item
from .forms import ItemForm

# Create your views here.

def index(request):
    item_list = Item.objects.all()
    context = {'item_list' : item_list,}
    return render(request, 'food/index.html', context)

def item(request):
    return HttpResponse("Hello world")

def detail(request, item_id):
    item = Item.objects.get(pk=item_id)
    context = {
        'item' : item,
    }
    return render(request, 'food/detail.html', context)

def create(request):
    form = ItemForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('food:index')
    
    return render(request, 'food/item-form.html', {'form': form})


def update(request, id):
    item = Item.objects.get(id=id)
    form = ItemForm(request.POST or None, instance=item)

    if form.is_valid():
        form.save()
        return redirect('food:index')
    
    return render(request, 'food/item-form.html', {'form': form, 'item':item})


def delete(request, id):
    item = Item.objects.get(id=id)

    if request.method == "POST":
        item.delete()
        return redirect('food:index')
    
    return render(request, 'food/item-delete.html', {'item':item})
