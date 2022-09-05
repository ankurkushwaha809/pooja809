# from unicodedata import name
from django.shortcuts import render, redirect

# Create your views here.
from django.http import HttpResponse
from kids_joy.models import Category

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
    employee = Category.objects.get(category_id=category_id)  
    return render(request,'edit_category.html', {'employee':employee})  

        # return render(request, 'edit_category.html')  

def update(request, category_id):  
    employee = Category.objects.get(category_id=category_id)  
    pooja = request.POST.get('ankur')
    employee.name = pooja
    employee.save()
    return redirect("/index")  