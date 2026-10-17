from rest_framework import serializers
from book.models import Book




class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'
        

# def one_to_five(value):
#     if not 0 <= value <= 5:
#         raise serializers.ValidationError('Рейтинг должен быть от 0 до 5')


# class RangeValidator:
#     def __init__(self, min_value, max_value):
#         self.min_value = min_value
#         self.max_value = max_value

#     def __call__(self, value):
#         if not self.min_value <= value <= self.max_value:
#             message = f'This field must be a between {self.min_value} and {self.max_value}.'
#             raise serializers.ValidationError(message)


# class BookSerializer(serializers.Serializer):
#     title = serializers.CharField(max_length=200, default='Django REST Framework')
#     author = serializers.CharField(max_length=100)
#     ratings = serializers.IntegerField(validators=[RangeValidator(0,5)])

#     def create(self, validated_data):
#         return Book.objects.create(**validated_data)

#     def update(self, instance, validated_data):
#         instance.title = validated_data.get("title", instance.title)
#         instance.author = validated_data.get("author", instance.author)
#         instance.save()
#         return instance

#     def validate(self, data):
#         if data['title'] == data['author']:
#             raise serializers.ValidationError("Введены одинаковые значения полей")
#         return data