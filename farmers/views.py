from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from rest_framework import viewsets  # add this
from .serializers import SellerSerializer, InventorySerializer  # add this
from .models import SellerProfile, Inventory  # add this
from rest_framework import filters


class InventoryView(viewsets.ModelViewSet):
    serializer_class = InventorySerializer
    queryset = Inventory.objects.all()
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['price']

    def get_queryset(self):
        queryset = Inventory.objects.all()
        crops = self.request.query_params.get('crops', None)
        if crops is not None:
            queryset = queryset.filter(crops=crops)
        queryset = queryset.order_by('price')
        return queryset


class SellerView(viewsets.ModelViewSet):
    serializer_class = SellerSerializer
    queryset = SellerProfile.objects.all()

    def get_queryset(self):
        queryset = SellerProfile.objects.all()
        id_ = self.request.query_params.get('id', None)
        if id is not None:
            queryset = queryset.filter(id=id_)
        return queryset
