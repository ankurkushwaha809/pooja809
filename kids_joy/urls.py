from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name= 'home1'),
    path('category', views.category, name='category'),
    path('index', views.index, name='index'),
    path('edit_category/<int:category_id>', views.edit_category, name='edit_category'),
    

]