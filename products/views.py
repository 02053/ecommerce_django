from django.shortcuts import render
from django.views.generic import View
from .models import Product, Category


class HomeView(View):
    def get(self, request, *args, **kwargs):
        template_name = 'products/index.html'
        model_products = Product.objects.all()
        model_category = Category.objects.all()
        context = {
            'products': model_products,
            'categories': model_category
        }

        return render(request, template_name, context)


class ProductDetailView(View):
    def get(self, request, *args, **kwargs):
        template_name = 'products/detail.html'
        product = Product.objects.get(slug=kwargs['slug'])
        context = {
            'product': product
        }

        return render(request, template_name, context)


class CategoriesSearchView(View):
    def get(self, request, *args, **kwargs):
        template_name = 'products/list.html'
        category_filter = Category.objects.get(slug=kwargs['slug'])
        model_category = Category.objects.all()
        model_products = Product.objects.filter(category=category_filter)
        context = {
            'products': model_products,
            'categories': model_category
        }

        return render(request, template_name, context)
