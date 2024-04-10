from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response

from . import IssueStatus
from .services.issue import IssueStatusService

from .models import Issue, IssueBonusPoint
from .serializers.issue import IssueSerializer, IssueChangeStatusSerializer, IssueCreateSerializer, \
    UserBonusPointsSerializer
from django.db import transaction
from .permissions import GetIssuePermissions


class IssueModelViewSet(viewsets.ModelViewSet):
    queryset = Issue.objects.all()
    serializer_class = IssueSerializer
    http_method_names = ['get', 'post', 'patch', 'delete']
    permission_classes = [permissions.IsAuthenticated]

    def get_serializer_class(self):
        if self.action == 'create':
            return IssueCreateSerializer

        return super().get_serializer_class()

    #
    def get_queryset(self):
        return GetIssuePermissions(self.queryset, self.request.user).get_issues()

    @transaction.atomic
    def create(self, request, *args, **kwargs):
        request.data['status'] = IssueStatus.choices[1][1]

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(creator=request.user)

        return Response(serializer.data, status=status.HTTP_201_CREATED)

    @transaction.atomic
    @action(
        methods=['post'],
        detail=False,
        serializer_class=IssueChangeStatusSerializer
    )
    def change_status(self, request, *args, **kwargs):
        issue_id = request.data.get('issue_id')
        try:
            issue = Issue.objects.get(pk=issue_id)
        except Issue.DoesNotExist:
            return Response({'status': 'Issue not found'}, status=400)

        current_status = issue.status
        next_statuses = IssueStatusService(issue).get_next_status()
        status_id = int(request.data.get('status_id'))

        try:
            if status_id not in [int(next_status) for next_status in next_statuses]:
                return Response({'status': 'Invalid status'}, status=400)

            new_status = IssueStatus.choices[status_id]
        except IndexError:
            return Response({'status': 'Status not found'}, status=400)

        if current_status == new_status:
            return Response({'status': 'Status not changed'}, status=400)

        issue.status = int(new_status[0])
        issue.save()
        if issue.status == int(IssueStatus.choices[5][0]):
            IssueBonusPoint.objects.create(issue=issue, user=issue.creator, point=200)

        return Response({'status': new_status[1]}, status=status.HTTP_200_OK)

    @action(
        methods=['get'],
        detail=False,
        serializer_class=UserBonusPointsSerializer
    )
    def my_bonus_points(self, request, *args, **kwargs):
        bonus_points = IssueBonusPoint.objects.filter(user=request.user)
        serializer = self.get_serializer(bonus_points, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
