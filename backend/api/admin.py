from django.contrib import admin

from .models import FoodCategory, Food


class FoodCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name_ru', 'name_en', 'name_ch', 'order_id')
    search_fields = ('id', 'name_ru', 'name_en', 'name_ch', 'order_id')
    empty_value_display = '-пусто-'


class FoodAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'category', 'is_vegan', 'is_special', 'code', 'internal_code', 'name_ru', 'description_ru',
        'description_en', 'description_ch', 'cost', 'is_publish')
    search_fields = ('id', 'category', 'is_vegan', 'is_special', 'code', 'internal_code', 'name_ru', 'description_ru',
                     'description_en', 'description_ch', 'cost', 'is_publish',)
    empty_value_display = '-пусто-'


admin.site.register(FoodCategory, FoodCategoryAdmin)
admin.site.register(Food, FoodAdmin)
