from rest_framework import serializers
from .models import GeneralSetting, GeneralSettingHeroImages, Section, Clients, SocialMediaLink, Modal, CounterItem
from utils.fields import CustomFileField

class GeneralSettingSerializer(serializers.ModelSerializer):
    hero_images = serializers.SerializerMethodField()
    social_media_links = serializers.SerializerMethodField()
    modals = serializers.SerializerMethodField()
    website_logo = CustomFileField()
    
    class Meta:
        model = GeneralSetting
        fields = [
            'website_title',
            'hero_text',
            'website_logo',
            'website_meta_description',
            'website_main_video',
            'contact_section_iframe_link',
            'website_email',
            'website_phone_number',
            'hero_images',
            'social_media_links',
            'modals'
        ]

    def get_hero_images(self, obj):
        images = GeneralSettingHeroImages.objects.all()
        return GeneralSettingHeroImageSerializer(images, many=True, context=self.context).data
    def get_social_media_links(self, obj):
        links = SocialMediaLink.objects.all().order_by('ordering')
        return SocialLinksSerializer(links, many=True, context=self.context).data
    def get_modals(self, obj):
        links = Modal.objects.all().order_by('ordering')
        return ModalSerializer(links, many=True, context=self.context).data

class GeneralSettingHeroImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = GeneralSettingHeroImages
        fields = ['id', 'image', 'left', 'right', 'top', 'bottom', 'mobile_width', 'desktop_width']

class SocialLinksSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialMediaLink
        fields = '__all__'

class ModalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Modal
        fields = '__all__'
        

class SectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Section
        fields = '__all__'
        
class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clients
        fields = '__all__'

class CounterSerializer(serializers.ModelSerializer):
    class Meta:
        model = CounterItem
        fields = '__all__'