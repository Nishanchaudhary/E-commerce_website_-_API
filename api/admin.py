from django.contrib import admin
from .models import Category, Product, Order, OrderItem

# Register the Category model
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id','image', 'name', 'description') 
    search_fields = ('name',)  
    list_filter = ('name',)  


# Register the Product model
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'category', 'stock','image', 'created_at')  
    search_fields = ('name', 'category__name')  
    list_filter = ('category', 'created_at')  
    list_editable = ('price', 'stock')  



class OrderItemInline(admin.TabularInline):  
    model = OrderItem
    extra = 1  


# Register the Order model
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'total_price', 'created_at')  
    search_fields = ('user__username',)  
    list_filter = ('created_at',) 
    inlines = (OrderItemInline,) 


# Register the OrderItem model separately (optional)
@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'order', 'product', 'quantity', 'price')  
    search_fields = ('order__id', 'product__name')  
    list_filter = ('order', 'product')  