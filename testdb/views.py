from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

from rest_framework import viewsets, permissions
from testdb.models import Products, Orders
from testdb.serializer import ProductsSerializer, OrdersSerializer
from testdb.serializer import UserSerializer
from testdb.permissions import IsOwnerOrReadOnly
from testdb.permissions import IsStaffOrTargetUser
from rest_framework import filters


# Create your views here.
class ProductsViewSet(viewsets.ModelViewSet):
    queryset = Products.objects.all().order_by('-name')
    serializer_class = ProductsSerializer
    filter_backends = [filters.SearchFilter,filters.OrderingFilter]
    ordering_fields = ['price']
    search_fields = ['name', 'category']
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
        IsOwnerOrReadOnly
    )

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class OrdersViewSet(viewsets.ModelViewSet):
    queryset = Orders.objects.all().order_by('-id')
    serializer_class = OrdersSerializer
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
        IsOwnerOrReadOnly
    )

    def get_queryset(self):
        user = self.request.user
        queryset = self.queryset.filter(owner=user)
        return queryset

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_permissions(self):
        return (permissions.AllowAny() if self.request.method == 'POST' else IsStaffOrTargetUser()),

    def perform_create(self, serializer):
        password = make_password(self.request.data['password'])
        serializer.save(password=password)

    def perform_update(self, serializer):
        password = make_password(self.request.data['password'])
        serializer.save(password=password)