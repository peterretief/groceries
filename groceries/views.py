from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render

from .models import Item


def detail(request, item_id):
    item = get_object_or_404(Item, pk=item_id)
    return render(request, 'groceries/detail.html', {'item': item})



def index(request):
    return HttpResponse("Hello, world. You're at the groceries index.")
