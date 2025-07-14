from django.contrib import admin

# Register your models here.
from .models import (
    Section,
    Clients,
    GeneralSetting,
    GeneralSettingHeroImages,
    CounterItem,
    SocialMediaLink,
    Modal
)

@admin.register(Section)
class SectionAdmin(admin.ModelAdmin):
    list_display = ['name', 'section_type', 'ordering']
    ordering = ['ordering']

@admin.register(Clients)
class ClientsAdmin(admin.ModelAdmin):
    list_display = ['name', 'ordering']
    ordering = ['ordering']

@admin.register(GeneralSetting)
class GeneralSettingAdmin(admin.ModelAdmin):
    list_display = ['website_title', 'website_email', 'website_phone_number']
    def has_add_permission(self, request):
        # Allow adding only if no instance exists
        return not GeneralSetting.objects.exists()

@admin.register(GeneralSettingHeroImages)
class GeneralSettingHeroImagesAdmin(admin.ModelAdmin):
    list_display = ['image', 'left', 'top', 'right', 'bottom', 'desktop_width', 'mobile_width']

@admin.register(CounterItem)
class CounterItemAdmin(admin.ModelAdmin):
    list_display = ['title', 'value']

@admin.register(SocialMediaLink)
class SocialMediaLinkAdmin(admin.ModelAdmin):
    list_display = ['name', 'link', 'ordering']
    ordering = ['ordering']

@admin.register(Modal)
class ModalAdmin(admin.ModelAdmin):
    list_display = ['modal_title', 'ordering']
    ordering = ['ordering']
