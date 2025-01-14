from django.shortcuts import render, redirect
from phones.models import Phone

def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    sort = request.GET.get("sort")
    phones =  Phone.objects.all()
    sorting = {'name': 'name', 'min_price': 'price', 'max_price': '-price'}
    if sort:
        phones =  Phone.objects.order_by(sorting[sort])
    context = {'phones': phones}
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phone =  Phone.objects.get(slug=slug)
    context = {'phone': phone}
    return render(request, template, context)