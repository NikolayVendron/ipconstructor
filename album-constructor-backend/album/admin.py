from django.contrib import admin
from .models import Review, Page, Size, Cover, Pattern, Order, Buyer
from import_export.admin import ImportExportModelAdmin

def in_progress(modeladmin, request, queryset):
    queryset.update(status='В процессе')
in_progress.short_description = "Изменить статус заказа 'В процессе'"

def completed(modeladmin, request, queryset):
    queryset.update(status='Выполнен')
completed.short_description = "Изменить статус заказа 'Выполнен'"

def canceled(modeladmin, request, queryset):
    queryset.update(status='Отменен')
canceled.short_description = "Изменить статус заказа 'Отменен'"

@admin.register(Order)
class OrderAdmin(ImportExportModelAdmin):
    list_display = ('pagesType', 'size', 'cover', 'pattern', 'pagesCount', 'buyer', 'status')
    search_fields = ("number__startswith",)
    actions = [in_progress, completed, canceled]
    pass

@admin.register(Buyer)
class BuyerAdmin(ImportExportModelAdmin):
    list_display = ('name', 'surname', 'number')
    search_fields = ("surname__startswith",)
    pass

admin.site.register(Size)
admin.site.register(Cover)
admin.site.register(Pattern)
admin.site.register(Page)
admin.site.register(Review)