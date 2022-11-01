from rest_framework import viewsets
from .models import List, Item
from .serializers import ItemSerializer, ListSerializer
from rest_framework import permissions, authentication


class ListViewset(viewsets.ModelViewSet):
    serializer_class = ListSerializer
    permission_classes = [permissions.IsAuthenticated]    
    authentication_classes = [authentication.TokenAuthentication, authentication.SessionAuthentication]
    

    def get_queryset(self):
        user = self.request.user
        return List.objects.filter(owner=user)


class ItemViewset(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    permission_classes = [permissions.IsAuthenticated]    
    authentication_classes = [authentication.TokenAuthentication, authentication.SessionAuthentication]
