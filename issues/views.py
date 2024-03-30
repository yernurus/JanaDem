from rest_framework import viewsets
from rest_framework.response import Response
from .services.issue import CreateIssueService

from .models import Issue
from .serializers.issue import IssueSerializer
# Create your views here.
class IssueModelViewSet(viewsets.ModelViewSet):
    queryset = Issue.objects.all()
    serializer_class = IssueSerializer
    http_method_names = ['get', 'post', 'patch', 'delete']

    def get_serializer_class(self):
        return super().get_serializer_class()
    
    def create(self, request, *args, **kwargs):
        create_service = CreateIssueService(self.queryset, self.serializer_class)
        return create_service.create(request, *args, **kwargs)
