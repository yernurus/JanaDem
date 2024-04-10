from django.db.models import Sum
from requests import request
from rest_framework import viewsets
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import api_view, action
from rest_framework_simplejwt.views import TokenObtainPairView

from .serializers.user import UserSerializer, UserCreateSerializer, UserUpdateSerializer
from .serializers.jwt import CustomTokenObtainPairSerializer

from .models import User
from issues.models import Issue, IssueBonusPoint
from issues.serializers.issue import IssueSerializer
from account import UserRole


class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

class UserModelViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    http_method_names = ['get', 'post', 'delete']

    def get_serializer_class(self):
        if self.action == 'create':
            return UserCreateSerializer
        elif self.action == 'partial_update':
            return UserUpdateSerializer
        return UserSerializer

    def create(self, request, *args, **kwargs):
        user_type = int(request.data.get('user_type'))
        if user_type == 1:
            request.data['user_type'] = UserRole.choices[0][0]
        elif user_type == 2:
            request.data['user_type'] = UserRole.choices[1][0]
        elif user_type == 3:
            request.data['user_type'] = UserRole.choices[2][0]

        serializer = UserCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        user.set_password(request.data['password'])
        user.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)
    @action(["get"], detail=False, serializer_class=UserSerializer, permission_classes=[IsAuthenticated])
    def request_user_info(self, request, *args, **kwargs):
        user = request.user
        serializer = self.get_serializer(user)

        return Response(serializer.data, status=status.HTTP_200_OK)


class IssueViewSet(viewsets.ModelViewSet):
    queryset = Issue.objects.all()
    serializer_class = IssueSerializer

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)

    def approve_issue(self, request, pk=None):
        issue = self.get_object()
        issue.status = 'approved'
        issue.save()
        return Response({'status': 'Issue approved'})

    def reject_issue(self, request, pk=None):
        issue = self.get_object()
        issue.status = 'rejected'
        issue.save()
        return Response({'status': 'Issue rejected'})

    def mark_as_in_process(self, request, pk=None):
        issue = self.get_object()
        issue.status = 'in_process'
        issue.save()
        return Response({'status': 'Issue marked as in process'})

    def mark_as_finished(self, request, pk=None):
        issue = self.get_object()
        issue.status = 'finished'
        issue.save()
        return Response({'status': 'Issue marked as finished'})
