from django.contrib import admin
from .models import Program, Elective, Contacts

# ------------------------------
# Program Admin
# ------------------------------
@admin.register(Program)
class ProgramAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    search_fields = ("name",)
    list_per_page = 25


# ------------------------------
# Elective Admin
# ------------------------------
@admin.register(Elective)
class ElectiveAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    search_fields = ("name",)
    list_per_page = 25


# ------------------------------
# Contacts Admin
# ------------------------------
@admin.register(Contacts)
class ContactsAdmin(admin.ModelAdmin):
    list_display = ("id", "first_name", "last_name", "email", "phone", "program", "elective", "created_at", "is_active")
    search_fields = ("first_name", "last_name", "email", "phone")
    list_filter = ("program", "elective", "is_active", "is_archive")
    readonly_fields = ("created_at", "updated_at", "slug")
    ordering = ("-created_at",)
    list_per_page = 25

    fieldsets = (
        ("Personal Info", {"fields": ("first_name", "last_name", "email", "phone", "age", "dob")}),
        ("Course Info", {"fields": ("course", "program", "elective")}),
        ("UTM Info", {"fields": ("utm_source", "utm_medium", "utm_campaign", "utm_device")}),
        ("System Info", {"fields": ("is_active", "is_archive", "slug", "created_at", "updated_at")}),
    )
