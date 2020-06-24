from django.urls import path
from sales import views

from . import views
from .views import SalesCreateView,SalesUpdateView,SalesDeleteView


urlpatterns = [
    path('', views.index, name="Home"),
    #path('emp/', views.emp, name="emp"),
    #path('show/', views.show, name="show"),
    #path('edit/<int:id>', views.edit, name="edit"),
    #path('update/<int:id>', views.update),
    #path('delete/<int:id>', views.destroy),
    
    path('add/', SalesCreateView.as_view(), name='add'),
    
    path('delete/<int:pk>/', SalesDeleteView.as_view(), name='delete'),
    
    path('update/<int:pk>/', SalesUpdateView.as_view(), name='update'),
    
    
]

