from account import permissions
from django.db.models import Q


class GetIssuePermissions:
    def __init__(self, queryset, user):
        self.queryset = queryset
        self.user = user

    def get_issues(self):
        queryset = self.queryset
        if permissions.IsSimpleUser().has_permission(self, self.user):
            return queryset.filter(creator=self.user)

        elif permissions.IsModerator().has_permission(self, self.user):
            return queryset.filter(Q(status__in=[1, 2, 3]) | Q(creator=self.user))

        elif permissions.IsAkim().has_permission(self, self.user):
            return queryset.filter(Q(status__in=[2, 4, 5]) | Q(creator=self.user))

        return queryset.none()
