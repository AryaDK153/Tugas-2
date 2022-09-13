from django.shortcuts import render
from katalog.models import CatalogItem

# TODO: Create your views here.
def show_katalog(request):
    data_item_katalog = CatalogItem.objects.all()
    context = {
        'list_item': data_item_katalog,
        'nama': 'Arya',
        'id': '2106702781'
    }
    return render(request, "katalog.html", context)