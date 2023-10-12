from rest_framework import serializers
from .models import Teacher, Student
from .verbose import val


class TeacherSerializer(serializers.ModelSerializer):

    class Meta:
        model = Teacher
        fields = "__all__"

    # name = serializers.CharField(max_length=155, min_length=5)
    # surname = serializers.CharField(min_length=5, max_length=255)
    # phone = serializers.CharField(validators=[val])
    #
    # def create(self, validated_data):
    #     return Teacher.objects.create(**validated_data)
    #
    # def validate_surnamer(self, value):
    #     if 'django' not in value.lower():
    #         raise serializers.ValidationError("Blog post is not about Django")
    #     return value
    #
    # def validate(self, data):
    #     if not data['phone'].startswith('+998'):
    #         raise serializers.ValidationError("write only uzb phone")
    #     return data


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"