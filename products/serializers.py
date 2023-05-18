from rest_framework import serializers

from .models import *

class SubCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SubCategory
        fields = '__all__'

    def to_representation(self, instance):
        product = self.context.get('product')
        if product.sub_category_id == instance.id:
            return super().to_representation(instance)
        return None

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ['image']

class CharacteristicsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Characteristics
        fields = ['left_side', 'right_side']

class ProductSerializer(serializers.ModelSerializer):
    images = ImageSerializer(many=True)
    sub_category = SubCategorySerializer()
    characteristics = CharacteristicsSerializer(many=True)

    class Meta:
        model = Product
        fields = '__all__'

    def to_representation(self, instance):
        self.fields['sub_category'].context['product'] = instance
        return super().to_representation(instance)

class CategorySerializer(serializers.ModelSerializer):
    category = ProductSerializer(many=True)
    sub_category = SubCategorySerializer(many=True)

    class Meta:
        model = Category
        fields = '__all__'
