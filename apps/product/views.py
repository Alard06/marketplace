from django.shortcuts import render

from apps.product.models import Category


# Create your views here.

def categories_list(request):
    categories = Category.objects.all()
    return render(request, context={'categories': categories}, template_name='product/categories.html')


def card_subcategory(request, slug):
    category = Category.objects.get(slug=slug)
    subcategory = category.subcategories.all()
    return render(request, context={'subcategory': subcategory}, template_name='product/subcategory.html')
