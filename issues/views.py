from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

from . import IssueStatus
from .services.issue import CreateIssueService

from .models import Issue
from .serializers.issue import IssueSerializer, IssueChangeStatusSerializer


class IssueModelViewSet(viewsets.ModelViewSet):
    queryset = Issue.objects.all()
    serializer_class = IssueSerializer
    http_method_names = ['get', 'post', 'patch', 'delete']

    def get_serializer_class(self):
        return super().get_serializer_class()

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)

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
        issue = get_object_or_404(Issue, pk=issue_id)

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
