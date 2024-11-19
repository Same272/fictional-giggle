from django.contrib import admin
from shop_app.models import CategoryProduct, Product, UserCart
@admin.register(CategoryProduct)
class CategoryAdminModel(admin.ModelAdmin):
    search_fields = ['category_name', 'id', 'created_at']
    list_filter = ['created_at']
    list_display = ['id', 'category_name', 'created_at']
    ordering = ['-id']

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    search_fields = ['product_name', 'id']
    list_filter = ['created_at']
    list_display = ['id', 'product_name', 'product_cost']
    ordering = ['-id']

@admin.register(UserCart)
class UserCartAdmin(admin.ModelAdmin):
    search_fields = ['id', 'user_id']
    list_filter = ['created_at']
    list_display = ['id', 'user_id', 'product']
    ordering = ['-id']