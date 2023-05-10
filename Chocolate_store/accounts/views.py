from django.contrib.auth import login
from rest_framework import generics, status, permissions
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response

from rest_framework.authtoken.models import Token

from .models import User
from .serializers import RegisterSerializer,LoginSerializer


class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]
    # renderer_classes = [TemplateHTMLRenderer]
    # template_name = 'register.html'


    def post(self,request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            # token,created =Token.objects.get_or_create(user=user)
            return Response(status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer
    permission_classes = [permissions.AllowAny]

    def post(self,request):
        serializer=self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user=serializer.validated_data['user']
        login(request,user)
        return Response(status=status.HTTP_201_CREATED)
