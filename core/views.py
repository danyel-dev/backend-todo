from rest_framework import viewsets
from .models import List, Item
from .serializers import ItemSerializer, ListSerializer
from rest_framework import permissions


class ListViewset(viewsets.ModelViewSet):
    queryset = List.objects.all()
    serializer_class = ListSerializer
    permission_classes = [permissions.IsAuthenticated]    

    
class ItemViewset(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    permission_classes = [permissions.IsAuthenticated]    
