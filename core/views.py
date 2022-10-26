from rest_framework import viewsets
from .models import List
from .serializers import ListSerializer
from rest_framework import permissions


class ListViewset(viewsets.ModelViewSet):
    queryset = List.objects.all()
    serializer_class = ListSerializer
    permission_classes = [permissions.IsAuthenticated]    
