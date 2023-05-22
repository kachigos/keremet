from rest_framework import serializers

from .models import *

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ['image']

class CharacteristicsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Characteristics
        fields = ['left_side', 'right_side']

class SubCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SubCategory
        fields = ('id','name',)

class CategorySerializer(serializers.ModelSerializer):
    sub_category = SubCategorySerializer(many=True)

    class Meta:
        model = Category
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    images = ImageSerializer(many=True)
    category = CategorySerializer()
    sub_category = SubCategorySerializer()
    characteristics = CharacteristicsSerializer(many=True)

    class Meta:
        model = Product
        fields = '__all__'

    def to_representation(self, instance):
        self.fields['sub_category'].context['product'] = instance
        return super().to_representation(instance)

