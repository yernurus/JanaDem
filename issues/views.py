from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response

from account.models import User
from . import IssueStatus
from .services.issue import CreateIssueService

from .models import Issue
from .serializers.issue import IssueSerializer, IssueChangeStatusSerializer, IssueCreateSerializer


class IssueModelViewSet(viewsets.ModelViewSet):
    queryset = Issue.objects.all()
    serializer_class = IssueSerializer
    http_method_names = ['get', 'post', 'patch', 'delete']

    def get_serializer_class(self):
        if self.action == 'create':
            return IssueCreateSerializer

        return super().get_serializer_class()

    def create(self, request, *args, **kwargs):
        request.data['creator'] = self.request.user.id
        request.data['status'] = IssueStatus.choices[0][1]

        print('data:', request.data)

        serializer = self.get_serializer(data=self.request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)

    # def send_issue(self, request, pk=None):
    #     issue = self.get_object()
    #     issue.status = 'sent'
    #     issue.save()
    #     return Response({'status': 'Issue sent'})
    #
    # def approve_issue(self, request, pk=None):
    #     issue = self.get_object()
    #     issue.status = 'approved'
    #     issue.save()
    #     return Response({'status': 'Issue approved'})
    #
    # def reject_issue(self, request, pk=None):
    #     issue = self.get_object()
    #     issue.status = 'rejected'
    #     issue.save()
    #     return Response({'status': 'Issue rejected'})
    #
    # def mark_as_in_process(self, request, pk=None):
    #     issue = self.get_object()
    #     issue.status = 'in_process'
    #     issue.save()
    #     return Response({'status': 'Issue marked as in process'})
    #
    # def mark_as_finished(self, request, pk=None):
    #     issue = self.get_object()
    #     issue.status = 'finished'
    #     issue.save()
    #     return Response({'status': 'Issue marked as finished'})

    @action(
        methods=['post'],
        detail=True,
        serializer_class=IssueChangeStatusSerializer
    )
    def change_status(self, request, *args, **kwargs):
        issue_id = kwargs.get('pk')
        try:
            issue = Issue.objects.get(pk=issue_id)
        except Issue.DoesNotExist:
            return Response({'status': 'Issue not found'}, status=400)

        current_status = issue.status
        status_id = int(request.data.get('status'))

        try:
            new_status = IssueStatus.choices[status_id]
        except IndexError:
            return Response({'status': 'Status not found'}, status=400)

        if current_status == new_status:
            return Response({'status': 'Status not changed'}, status=400)

        issue.status = new_status
        issue.save()

        return Response({'status': issue.status[1]}, status=status.HTTP_200_OK)
