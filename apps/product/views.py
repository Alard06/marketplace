from django.http import HttpResponse
from django.shortcuts import render, redirect

from apps.product.models import Category, Product, SubCategory, CartItem


# Create your views here.

def categories_list(request):
    categories = Category.objects.all()
    return render(request, context={'categories': categories}, template_name='product/categories.html')


def card_subcategory(request, slug):
    category = Category.objects.get(slug=slug)
    subcategory = category.subcategories.all()
    return render(request, context={'subcategory': subcategory}, template_name='product/subcategory.html')


def product_list(request, slug):
    subcategory = SubCategory.objects.get(slug=slug)
    products = subcategory.products.all()
    context = {'products': products}
    return render(request, context=context, template_name='product/cart_list.html')


def view_cart(request):
    cart_items = CartItem.objects.filter(user=request.user)
    total_price = sum(item.product.price * item.quantity for item in cart_items)
    return render(request, template_name='product/cart.html',
                  context={'cart_items': cart_items, 'total_price': total_price})


def add_to_cart(request, product_id):
    product = Product.objects.get(id=product_id)
    cart_item, created = CartItem.objects.get_or_create(product=product,
                                                        user=request.user)
    cart_item.quantity += 1
    cart_item.save()
    return redirect('view_cart')


def remove_from_cart(request, item_id):
    cart_item = CartItem.objects.get(id=item_id)
    cart_item.delete()
    return redirect('view_cart')
