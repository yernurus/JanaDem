from rest_framework import serializers
from ..models import Issue, IssueBonusPoint
from issues import IssueStatus
from account.serializers.user import UserSerializer
from ..services.issue import IssueStatusService

#Serializer for Issue
class IssueSerializer(serializers.ModelSerializer):
    status = serializers.CharField(source='get_status_display')
    creator = UserSerializer(read_only=True)
    next_statuses = serializers.SerializerMethodField()

    #function for defining next available status
    def get_next_statuses(self, obj):
        current_status = obj.status
        next_statuses = IssueStatusService(obj, self.context['request'].user.user_type).get_next_status()

        data = []
        for next_status in next_statuses:
            next_status = int(next_status)
            data.append({'id': IssueStatus.choices[next_status][0], 'status': IssueStatus.choices[next_status][1]})

        return data

    class Meta:
        model = Issue
        fields = ['id', 'image', 'title', 'description', 'longitude', 'latitude', 'status', 'creator', 'next_statuses']

#Serializer for creating Issue
class IssueCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Issue
        fields = ['image', 'title', 'description', 'longitude', 'latitude']

#Serizlizer for changing Issue details
class IssueChangeStatusSerializer(serializers.Serializer):
    issue_id = serializers.IntegerField()
    status_id = serializers.IntegerField()


#Serializer for earning Bonus points when User's Issue gets finished
class UserBonusPointsSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S')

    class Meta:
        model = IssueBonusPoint
        fields = ['issue', 'point', 'created_at']
