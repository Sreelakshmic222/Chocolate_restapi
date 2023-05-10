from django.shortcuts import redirect
from rest_framework import generics, permissions, status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from knox.models import AuthToken
from rest_framework.views import APIView

from .serializers import  CartSerializer, FavoriteSerializer
from django.contrib.auth import login

from rest_framework import permissions
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.views import LoginView as KnoxLoginView
#for CRUD
from .models import Chocolate, Cart, Favorite
from .serializers import ChocoSerializer
from rest_framework import generics
#html render
from rest_framework.renderers import TemplateHTMLRenderer

# # Register API
# class RegisterAPI(generics.GenericAPIView):
#     serializer_class = RegisterSerializer
#
#     def post(self, request, *args, **kwargs):
#         serializer = self.get_serializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         user = serializer.save()
#         return Response({
#         "user": UserSerializer(user, context=self.get_serializer_context()).data,
#         "token": AuthToken.objects.create(user)[1]
#         })
# class LoginAPI(KnoxLoginView):
#     permission_classes = (permissions.AllowAny,)
#
#     def post(self, request, format=None):
#         serializer = AuthTokenSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         user = serializer.validated_data['user']
#         login(request, user)
#         return super(LoginAPI, self).post(request, format=None)

class ListChocos(generics.ListCreateAPIView):
    permission_classes = [AllowAny]
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'list.html'
    queryset = Chocolate.objects.all()
    serializer_class = ChocoSerializer


    def list(self,request,**kwargs):
        queryset = self.get_queryset()
        return Response({'object_list':queryset})

class DetailChoco(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'detail.html'
    queryset = Chocolate.objects.all()
    serializer_class = ChocoSerializer

    def get(self,request,*args,**kwargs):
        # cusom GET method
        queryset = self.get_object()
        if queryset is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        authenticated=request.user.is_authenticated
        print('#####',authenticated)
        if not authenticated:
            return redirect('list')
        return Response({'object':queryset,'authenticated':authenticated})

# class UpdateChoco(generics.UpdateAPIView):
#     queryset = Chocolate.objects.all()
#     serializer_class = ChocoSerializer
#
#     def put(self, request, pk):
#         return self.update(request,pk)

class Checkoutview(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'checkout.html'
    queryset = Chocolate.objects.all()
    serializer_class = ChocoSerializer

    def get(self,request,*args,**kwargs):
        #your custom GET method logic here
        queryset=self.get_object()

        #serializer=self.get_serializer(queryset)
        return Response({'object':queryset})

class AddToCartView(generics.CreateAPIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'cart.html'
    queryset = Cart.objects.all()
    serializer_class = CartSerializer

    def perform_create(self, serializer):
        product = Chocolate.objects.get(pk=self.kwargs['pk'])
        cart = self.get_queryset().first()
        if not cart:
            cart = Cart.objects.create()
        cart.items.add(product)
        serializer.save(items=cart.items.all())

        def get(self, request, *args, **kwargs):
            # your custom GET method logic here
            queryset = self.get_object()
            # serializer=self.get_serializer(queryset)
            return Response({'cart_items': queryset})



class AddToFavoriteView(generics.CreateAPIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'favorite.html'
    queryset = Favorite.objects.all()
    serializer_class = FavoriteSerializer

    def get(self,request,*args,**kwargs):
        #your custom GET method logic here
        queryset=self.get_object()
        #serializer=self.get_serializer(queryset)
        return Response({'fav_items':queryset})

class HomePageView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'homepage.html'

    def get(self, request):
        # Your view logic here
        return Response({'message':'Welcome'})