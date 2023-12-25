from django.shortcuts import render, redirect
from pages.forms import ReservationForm
from pages.models import ScrollModel, GalleryModel, MenuModel
# Create your views here.

def home_page_view(request):
    scrolls = ScrollModel.objects.all().order_by('-pk')[:5]
    gallery = GalleryModel.objects.all().order_by('-pk')
    burger = MenuModel.objects.filter(category__title__icontains ='Burger').order_by('-pk')
    pizza = MenuModel.objects.filter(category__title__icontains ='Pizza').order_by('-pk')
    frices = MenuModel.objects.filter(category__title__icontains ='Frice').order_by('-pk')
    salads = MenuModel.objects.filter(category__title__icontains ='Salad').order_by('-pk')
    drinks = MenuModel.objects.filter(category__title__icontains ='Drink').order_by('-pk')
  


    context = {
        'scrolls': scrolls,
        'galleries': gallery,
        "burgers": burger,
        "pizzas": pizza,
        "frices": frices,
        "salads": salads,
        "drinks": drinks
    }
    
    return render(request, template_name='index.html',context=context)


def reservation_view(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('http://127.0.0.1:8000/')  
    else:
        form = ReservationForm()
    
    return render(request, template_name='index.html')

