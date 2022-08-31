# from unicodedata import name
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

from .models import Category

def home(request):
    # return HttpResponse("Hello, world. You're at the polls index.")
    return render(request, 'home.html')

def index(request):
    categorys =  Category.objects.all() 
    return render(request, 'index.html', {'categorys': categorys})


def category(request):

    if request.method == 'POST' :
        # breakpoint()
        pooja = request.POST.get('ankur')
        pooja = Category(name=pooja)
        pooja.save()
    return render(request, 'category.html')

def edit_category(request, category_id):
    breakpoint()
    category_id = int(category_id)
    try:
        category_sel = Category.objects.get(category_id = category_id)
    except Category.DoesNotExist:
        return redirect('index')
    category_form = Category(request.POST.get('ankur') or None, category_sel)
    # if category_form.is_valid():
    category_form.save()
    return render(request, 'edit_category.html', {'category_form':category_form})
    # return render(request, 'edit_category.html')