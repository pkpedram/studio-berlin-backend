from django.db import models
from django.core.exceptions import ValidationError


# Create your models here.
class Section(models.Model):
    name = models.CharField(blank=False, null=False)
    content = models.TextField(blank=True, null=True)
    ordering = models.IntegerField(default=0, null=False, blank=False)
    class SectionType(models.TextChoices):
        CONTENT = 'content'
        PROJECTS = 'projects'
        SERVICES = 'services'
        CONTACT = 'contact'
        COUNTER = 'counter'
        CLIENTS = 'clients'
      
    section_type = models.CharField(
        max_length=20,
        choices=SectionType.choices,
        default=SectionType.CONTENT
    )
    def __str__(self):
        return f"{self.name}"

    def clean(self):
        if self.section_type == self.SectionType.CONTACT and not self.content:
            raise ValidationError("Content field is empty")
      

    def save(self, *args, **kwargs):
        self.full_clean()  # calls `clean()` method above
        super().save(*args, **kwargs)
        
class Clients(models.Model):
    name = models.CharField(blank=False, null=False)
    logo = models.ImageField(blank=False, null=False)
    ordering = models.IntegerField(default=0, null=False, blank=False)
    
    def __str__(self):
        return f"{self.name}"
    
class GeneralSetting(models.Model):
    website_title = models.CharField(blank=False)
    hero_text = models.CharField(blank=True)
    website_logo = models.ImageField(upload_to='shared_media/')
    website_meta_description = models.CharField(blank=True)
    website_main_video = models.CharField(blank=True)
    contact_section_iframe_link = models.CharField(blank=True)
    website_email = models.EmailField(blank=True)
    website_phone_number = models.CharField(blank=True)
    
class GeneralSettingHeroImages(models.Model):
    image = models.ImageField(upload_to='shared_media/')
    left = models.CharField(blank=True, null=True)
    right = models.CharField(blank=True, null=True)
    top = models.CharField(blank=True, null=True)
    down = models.CharField(blank=True, null=True)
    
class CounterItem(models.Model):
    title = models.CharField(blank=False, null=False)
    description = models.TextField(blank=True, null=True)
    value = models.IntegerField(default=0)
    ordering = models.IntegerField(default=0, blank=False, null=False)
    
    
class SocialMediaLink(models.Model):
    name = models.CharField(null=False, blank=False)
    icon = models.ImageField(upload_to='shared_media/', null=True)
    link = models.URLField(blank=False, null=False)
    ordering = models.IntegerField(default=0)

class Modal(models.Model):
    modal_title = models.CharField(null=False, blank=False)
    modal_content = models.TextField(null=False, blank=False)
    ordering = models.IntegerField(default=0)