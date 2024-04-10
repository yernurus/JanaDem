from rest_framework.response import Response
from rest_framework import status

from issues import IssueStatus


class CheckIsValidFile:
    def __init__(self, file):
        self.file = file
    
    def check(self) -> bool:
        file = self.file.name.split('.')[-1]
        if file in ['jpg', 'jpeg', 'png', 'heic', 'svg']:
            return True
        return False


class CreateIssueService:
    def __init__(self, queryset, serializer):
        self.queryset = queryset
        self.serializer = serializer
    
    def create(self, request, *args, **kwargs):
        data = request.data

        check_file_service = CheckIsValidFile(data['image'])
        if check_file_service.check():
            serializer = self.serializer(data=data)
            serializer.is_valid(raise_exception=True)
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response({'message': "File doesn't match valid format!"}, status=status.HTTP_400_BAD_REQUEST)


class IssueStatusService:
    def __init__(self, issue):
        self.issue = issue
        self.choices = IssueStatus.choices

    def get_next_status(self):
        current_status = self.issue.status
        next_statuses = []

        if current_status == self.choices[0][0] or current_status == self.choices[1][0]:
            next_statuses = [self.choices[2][0], self.choices[3][0]]
        if current_status == self.choices[2][0]:
            next_statuses = [self.choices[4][0]]
        if current_status == self.choices[4][0]:
            next_statuses = [self.choices[5][0]]

        return next_statuses
