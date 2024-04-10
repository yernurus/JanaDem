from rest_framework import serializers
from ..models import Issue
from issues import IssueStatus
from account.serializers.user import UserSerializer


class IssueSerializer(serializers.ModelSerializer):
    status = serializers.CharField(source='get_status_display')
    creator = UserSerializer(read_only=True)

    class Meta:
        model = Issue
        fields = ['id', 'image', 'title', 'description', 'longitude', 'latitude', 'status', 'creator']


class IssueCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Issue
        fields = ['image', 'title', 'description', 'longitude', 'latitude']


class IssueChangeStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Issue
        fields = ['id', 'status']
