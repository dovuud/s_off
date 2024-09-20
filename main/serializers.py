from rest_framework import serializers

from .models import *

class WhyUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = WhyUs
        fields = '__all__'

class PartnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Partners
        fields = '__all__'

class LaptopSerializer(serializers.ModelSerializer):
    class Meta:
        model = Laptops
        fields = '__all__'

class FAQSerializer(serializers.ModelSerializer):
    class Meta:
        model = FAQs
        fields = '__all__'

class AboutSerializer(serializers.ModelSerializer):
    class Meta:
        model = About
        fields = '__all__'

class Program_infoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Programm_info
        fields = '__all__'

class ProgrammsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Programms
        fields = ['id', 'title', 'title_en', 'title_ru', 'title_uz', 'description', 'description_en', 'description_ru', 'description_uz', 'extr_info']
