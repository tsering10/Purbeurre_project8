from django.urls import path
from django.views.generic import TemplateView

from . import views

urlpatterns = [
    path('search/', views.search, name='search'),
    path('contacts/', views.contacts, name='contacts'),
    path('legal/',views.legal,name='legal'),
    path('<int:id_product>',views.detail, name='product_detail'),
]