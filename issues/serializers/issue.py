from rest_framework import serializers
from ..models import Issue


class IssueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Issue
        fields = '__all__'


class IssueCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Issue
        fields = ['image', 'title', 'description', 'longitude', 'latitude']


class IssueChangeStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Issue
        fields = ['id', 'status']
