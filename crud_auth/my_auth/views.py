import imp
from django.shortcuts import render
from rest_framework import generics
from .serializers import UserSerializer,CartSerializer
from .models import Cart
from django.contrib.auth.models import User
from rest_framework import permissions
from .permissions import IsOwnerOrReadOnly
from rest_framework import mixins
# Create your views here
class UserList(generics.ListAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()

class UserRetrive(generics.RetrieveAPIView):
    serializer_class=UserSerializer
    queryset = User.objects.all()

class CartAddRetrive(generics.ListCreateAPIView):
    serializer_class =CartSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Cart.objects.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class CartUpdateDelete(generics.RetrieveUpdateDestroyAPIView,mixins.UpdateModelMixin):
    serializer_class  = CartSerializer
    queryset = Cart.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly]


    def put(self, request, *args, **kwargs):
        return self.update(request,partial=True,*args,**kwargs)


