from django.db import models
from django.core.exceptions import ValidationError
# Create your models here.

class ProjectCategory(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    ordering = models.IntegerField(default=0, blank=False, null=False)

    def __str__(self):
        return self.name
    
    
class Project(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    ordering = models.IntegerField()
    thumbnail = models.ImageField(upload_to="thumbnails/")
    slug = models.SlugField(unique=True, blank=True)

    def __str__(self) -> str:
        return self.name
    
class ProjectRelatedCategory(models.Model):
    related_project = models.ForeignKey(to=Project, on_delete=models.CASCADE)
    related_category = models.ForeignKey(to=ProjectCategory, on_delete=models.CASCADE)
    ordering = models.IntegerField()
    
    
class ProjectCategoryImage(models.Model):
    image = models.ImageField(upload_to='project_category_images/')
    related_category = models.ForeignKey(to=ProjectCategory, on_delete=models.CASCADE)
    
class ProjectMedia(models.Model):
    class MediaType(models.TextChoices):
        IFRAME = 'iframe'
        IMAGE = 'image'
        VIDEO = 'video'
        VIMEO = 'vimeo'
      
    media_type = models.CharField(
        max_length=20,
        choices=MediaType.choices,
        default=MediaType.IMAGE
    )
    video =models.FileField(upload_to='project_videos/', blank=True, null=True)
    iframe_link = models.CharField(blank=True, null=True)
    vimeo_video_id = models.CharField(blank=True, null=True)
    image = models.ImageField(upload_to="project_images/", blank=True, null=True)
    related_project = models.ForeignKey(to=Project, on_delete=models.CASCADE, null=True)
    
    def __str__(self):
        return f"{self.media_type} media"

    def clean(self):

        if self.media_type == self.MediaType.IMAGE and not self.image:
            raise ValidationError("Image is required for media_type 'image'.")
        if self.media_type == self.MediaType.VIDEO and not self.video:
            raise ValidationError("Video link is required for media_type 'video'.")
        if self.media_type == self.MediaType.IFRAME and not self.iframe_link:
            raise ValidationError("Iframe link is required for media_type 'iframe'.")
        if self.media_type == self.MediaType.VIMEO and not self.vimeo_video_id:
            raise ValidationError("Vimeo ID is required for media_type 'vimeo'.")

    def save(self, *args, **kwargs):
        self.full_clean()  # calls `clean()` method above
        super().save(*args, **kwargs)