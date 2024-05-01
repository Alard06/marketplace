from django.contrib import admin

from apps.product.models import Product, Category, SubCategory



@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', )


@admin.register(SubCategory)
class SubCategoryAdmin(admin.ModelAdmin):
    pass