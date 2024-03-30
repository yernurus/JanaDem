from rest_framework.response import Response
from rest_framework import status


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