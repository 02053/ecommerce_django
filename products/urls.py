from django.urls import path
from .views import HomeView, CategoriesSearchView, ProductDetailView

app_name = 'products'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('<slug:slug>/', CategoriesSearchView.as_view(), name='list'),
    path('detail/<slug:slug>/', ProductDetailView.as_view(), name='detail'),
]
