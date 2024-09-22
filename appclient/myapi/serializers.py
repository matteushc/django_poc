from rest_framework import serializers

from .models import AppClient

class AppClientSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AppClient
        fields = ('postId', 'name', 'email', 'body')