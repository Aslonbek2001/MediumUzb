# admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

class CustomUserAdmin(UserAdmin):
    model = User
    # Admin panelida foydalanuvchi ma'lumotlarini qanday ko'rsatishni belgilash
    list_display = ('username', 'email', 'rule', 'phone_number', 'date_of_birth', 'profession', 'experience', 'profile_image', 'created_at', 'updated_at', 'is_active')
    list_filter = ('rule', 'is_active', 'date_of_birth')  # Filtrlash uchun maydonlar
    search_fields = ('username', 'email', 'phone_number')  # Qidirish uchun maydonlar
    ordering = ('username',)  # Tartiblashtirish

    # Foydalanuvchi qo'shish va o'zgartirish sahifasidagi maydonlar
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'email', 'phone_number', 'date_of_birth', 'profession', 'experience', 'bio', 'profile_image', 'github_link', 'linkedin_link', 'twitter_link')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'rule')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2', 'email', 'rule', 'is_active', 'is_staff', 'phone_number', 'date_of_birth', 'profession', 'experience', 'bio', 'profile_image', 'github_link', 'linkedin_link', 'twitter_link')}
        ),
    )


admin.site.register(User, CustomUserAdmin)
