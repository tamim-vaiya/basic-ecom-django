from django.contrib import admin
from .models import Product, Order

# Register your models here.
admin.site.site_header = "E-commerce Site"
admin.site.site_title = "The Goods Co."
admin.site.index_title = "Manage The Goods Co."

class ProductAdmin(admin.ModelAdmin):

    def change_category_to_default(self, request, queryset):
        queryset.update(category="default")

    change_category_to_default.short_description = "Default Category"
    list_display = ('title', 'price', 'discount_price', 'category', 'description',)
    search_fields = ('title', 'category',)
    actions = ('change_category_to_default',)
    # fields = ('title', 'category')
    list_editable = ('price', 'discount_price', 'category',)

admin.site.register(Product, ProductAdmin)
admin.site.register(Order)