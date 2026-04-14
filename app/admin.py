from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

from .models import Car, Order, OrderLine, Service, CarComment


class orderLineInstanceInline(admin.TabularInline):
    model = OrderLine
    readonly_fields = ["service"]
    can_delete = False
    extra = 0
    fields = ["order", "service", "quantity"]


class carAdmin(admin.ModelAdmin):
    list_display = ["make", "model",
                    "client_name", "license_plate", "vin_code", "cover"]
    search_fields = ["license_plate", "vin_code"]
    list_filter = ["client_name", "make", "model"]


class orderAdmin(admin.ModelAdmin):
    list_display = ["date", "car",  "status", "due_back"]
    inlines = [orderLineInstanceInline]
    list_editable = ["status"]


class orderLineAdmin(admin.ModelAdmin):
    list_display = ["order", "service", "quantity"]
    list_editable = ["quantity", "service"]


class serviceAdmin(admin.ModelAdmin):
    list_display = ["name", "price"]
    list_editable = ["price"]


class CarCommentAdmin(admin.ModelAdmin):
    list_display = ["car", "date_created", "client"]


class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        ('Additional Info', {'fields': ('photo',)}),
    )


admin.site.register(Car, carAdmin)
admin.site.register(Order, orderAdmin)
admin.site.register(OrderLine, orderLineAdmin)
admin.site.register(Service, serviceAdmin)
admin.site.register(CarComment, CarCommentAdmin)
admin.site.register(CustomUser, CustomUserAdmin)
