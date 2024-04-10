from rest_framework import serializers
from ..models import Issue, IssueBonusPoint
from issues import IssueStatus
from account.serializers.user import UserSerializer
from ..services.issue import IssueStatusService


class IssueSerializer(serializers.ModelSerializer):
    status = serializers.CharField(source='get_status_display')
    creator = UserSerializer(read_only=True)
    next_statuses = serializers.SerializerMethodField()

    def get_next_statuses(self, obj):
        current_status = obj.status
        next_statuses = IssueStatusService(obj).get_next_status()

        data = []
        for next_status in next_statuses:
            next_status = int(next_status)
            data.append({'id': IssueStatus.choices[next_status][0], 'status': IssueStatus.choices[next_status][1]})

        return data

    class Meta:
        model = Issue
        fields = ['id', 'image', 'title', 'description', 'longitude', 'latitude', 'status', 'creator', 'next_statuses']


class IssueCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Issue
        fields = ['image', 'title', 'description', 'longitude', 'latitude']


class IssueChangeStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Issue
        fields = ['id', 'status']


class UserBonusPointsSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    issue = IssueSerializer(read_only=True)
    created_at = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S')

    class Meta:
        model = IssueBonusPoint
        fields = ['user', 'issue', 'point', 'created_at']
