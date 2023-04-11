from django.shortcuts import render, redirect, get_object_or_404
from .models import Item
from .forms import ItemForm
# Create your views here.


def get_shop_list(request):
    items = Item.objects.all()
    context = {
        'items': items
    }
    return render(request, 'shop/shop_list.html', context)


def add_item_shop_list(request):
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('get_shop_list')
    form = ItemForm()  # create an instance
    context = {
        'form': form
        }
    return render(request, 'shop/add_item_shop_list.html', context)


def edit_item_shop_list(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    if request.method == 'POST':
        form = ItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('get_shop_list')
    form = ItemForm(instance=item)  # create an instance pre filled with data got from DB
    context = {
        'form': form
        }
    return render(request, 'shop/edit_item_shop_list.html', context)