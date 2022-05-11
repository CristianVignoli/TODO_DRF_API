from django.contrib.auth.models import User
from rest_framework import serializers
from drf_extra_fields.fields import Base64ImageField
from .models import TODOItem


class RegistrationSerializer(serializers.ModelSerializer):
    email = serializers.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}
    
    def create(self, data):
        return User.objects.create_user(
            username=data['username'],
            email=data['email'],
            password=data['password']
        )


class TODOItemSerializer(serializers.HyperlinkedModelSerializer):
    image = Base64ImageField()

    class Meta:
        model = TODOItem
        fields = [
            'title',
            'description',
            'image',
            'deadline',
            'creation_date',
            'url'
        ]
    
    def create(self, data):
        return TODOItem.objects.create(
            owner=data['owner'],
            title=data['title'],
            description=data['description'],
            image=data['image'],
            deadline=data.get('deadline', None)
        )