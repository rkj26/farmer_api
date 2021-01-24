from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from rest_framework import viewsets  # add this
from .serializers import SellerSerializer, InventorySerializer, UserSerializer, CartSerializer, \
    OrderHistorySerializer, ImageSerializer  # add this
from .models import SellerProfile, Inventory, UserProfile, Cart, OrderHistory, Image  # add this
from rest_framework import filters
from django.contrib.gis.measure import D
from django.contrib.gis.db.models.functions import Distance
from django.contrib.gis.geos import Point
from datetime import datetime, timedelta, time


class InventoryView(viewsets.ModelViewSet):
    serializer_class = InventorySerializer
    queryset = Inventory.objects.all()
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['price']

    def get_queryset(self):
        distance = 10000
        queryset = Inventory.objects.all()
        crops = self.request.query_params.get('crops', None)
        latitude = self.request.query_params.get('latitude', None)
        longitude = self.request.query_params.get('longitude', None)
        if latitude and longitude:
            ref_location = Point(float(latitude), float(longitude))
            queryset = Inventory.objects.filter(location__distance_lte=(ref_location, D(m=distance))).annotate(
                distance=Distance('location', ref_location)).order_by('distance')

        if crops is not None:
            queryset = queryset.filter(crops=crops)

        return queryset


class SellerView(viewsets.ModelViewSet):
    serializer_class = SellerSerializer
    queryset = SellerProfile.objects.all()

    def get_queryset(self):
        queryset = SellerProfile.objects.all()
        id_ = self.request.query_params.get('id', None)
        if id_ is not None:
            queryset = queryset.filter(id=id_)
        return queryset


class UserView(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = UserProfile.objects.all()

    def get_queryset(self):
        queryset = UserProfile.objects.all()
        id_ = self.request.query_params.get('id', None)
        if id_ is not None:
            queryset = queryset.filter(id=id_)
        return queryset


class CartView(viewsets.ModelViewSet):
    serializer_class = CartSerializer
    queryset = Cart.objects.all()

    def get_queryset(self):
        queryset = Cart.objects.all()
        id_ = self.request.query_params.get('id', None)
        if id_ is not None:
            queryset = queryset.filter(user=id_)
        return queryset


class OrderHistoryView(viewsets.ModelViewSet):
    serializer_class = OrderHistorySerializer
    queryset = OrderHistory.objects.all()

    def get_queryset(self):
        queryset = OrderHistory.objects.all()
        id_ = self.request.query_params.get('id', None)
        today = datetime.now().date()+timedelta(1)
        queryset = OrderHistory.objects.filter(when__gte=today - timedelta(days=26), when__lt=today)
        if id_ is not None:
            queryset = queryset.filter(seller=id_)
        return queryset

class ImageView(viewsets.ModelViewSet):
    serializer_class = ImageSerializer
    queryset = Image.objects.all()