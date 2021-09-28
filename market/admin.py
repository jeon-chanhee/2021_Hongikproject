from django.contrib import admin
from market.models import Product, Recommendation, Store


@admin.register(Recommendation)
class RecommendationAdmin(admin.ModelAdmin):
    list_display = ['person']


@admin.register(Store)
class StoreAdmin(admin.ModelAdmin):
    list_display = ['name', 'tel', 'opentime', 'closetime']


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'intro']
