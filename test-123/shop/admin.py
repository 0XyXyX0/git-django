from django.contrib import admin
from shop.models import Tag, Item, Category
from shop.filters import PriceFilter


class TagItemInLine(admin.StackedInline):
    model = Tag.items.through
    extra = 1

class ItemInLine(admin.StackedInline):
    model = Item
    extra = 1

class TagInLine(admin.StackedInline):
    model = Item.tags.through
    extra = 1

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', "get_five_items"]
    search_fields = ['name', 'id', 'items__name']
    ordering = ['id']
    list_per_page = 100
    inlines = [ItemInLine]

    # def get_five_items(self, category):
    #     items = category.items.all()[:5]
    #     empty_list = []
    #     for item in items:
    #         empty_list.append(item.name)
    #     return empty_list if empty_list else "No items found"
    
    def get_five_items(self, category):
        result_list = [item.name for item in category.items.all()[:5]]
        return result_list if result_list else "No items found"


    def get_queryset(self, request):
        existing_queryset = super().get_queryset(request)
        return existing_queryset.prefetch_related('items')

class ItemAdmin(admin.ModelAdmin):
    search_fields = ['name']
    ordering = ['price']
    list_display = ['id', 'name', 'price']
    autocomplete_fields = ['category']
    fields = ['name', 'price', 'description', 'category']
    list_per_page = 100
    list_filter = [PriceFilter]
    inlines = [TagInLine]

class TagAdmin(admin.ModelAdmin):
    list_display = ['name', 'id']
    search_fields = ['name']
    inlines = [TagItemInLine]

admin.site.register(Category, CategoryAdmin)
admin.site.register(Item, ItemAdmin)
admin.site.register(Tag, TagAdmin)

