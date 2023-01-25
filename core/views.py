from .models import List
from rest_framework import viewsets
from rest_framework import permissions
from .Serializers import ListSerializer


class ListViewSet(viewsets.ModelViewSet):
    queryset = List.objects.all()
    serializer_class = ListSerializer
    permission_classes = [permissions.IsAuthenticated]
