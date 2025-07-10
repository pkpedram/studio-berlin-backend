from rest_framework import serializers
from .models import ProjectCategory, ProjectCategoryImage, Project, ProjectMedia

class ProjectCategorySerializer(serializers.ModelSerializer):
    images = serializers.SerializerMethodField()
    class Meta: 
        model = ProjectCategory
        fields = [
            'name',
            'description',
            'ordering',
            'images'
        ]
    def get_images(self, obj):
        request = self.context.get('request')
        images = ProjectCategoryImage.objects.filter(related_category=obj)
        return [
            request.build_absolute_uri(image.image.url) if request else image.image.url
            for image in images
        ]

class ProjectCategoryImagesSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ProjectCategoryImage
        fields = [
            'image'
        ]
        
class ProjectMediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectMedia
        fields = ['media_type', 'video', 'iframe_link', 'vimeo_video_id', 'image']

class ProjectSerializer(serializers.ModelSerializer):
    categories = serializers.SerializerMethodField()
    class Meta:
        model = Project
        fields = ['id', 'name', 'slug', 'description', 'created_at', 'updated_at', 'ordering', 'thumbnail', 'categories']
        
    def get_categories(self, obj):
        categories = ProjectCategory.objects.filter(
        projectrelatedcategory__related_project=obj
        ).distinct().values_list('name', flat=True)
        return list(categories)

class ProjectDetailSerializer(ProjectSerializer):
    media = serializers.SerializerMethodField()
    categories = serializers.SerializerMethodField()

    class Meta(ProjectSerializer.Meta):
        fields = ProjectSerializer.Meta.fields + ['media', 'categories']

    def get_media(self, obj):
        request = self.context.get('request')
        media_qs = ProjectMedia.objects.filter(related_project=obj)
        return ProjectMediaSerializer(media_qs, many=True, context={'request': request}).data
    
    def get_categories(self, obj):
        categories = ProjectCategory.objects.filter(
        projectrelatedcategory__related_project=obj
        ).distinct().values_list('name', flat=True)
        return list(categories)