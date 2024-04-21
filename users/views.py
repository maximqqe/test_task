import secrets
import string

from django.contrib.auth import login
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken

from .models import CustomUser
from .serializers import PhoneNumberSerializer, VerificationSerializer, UserSerializer
from rest_framework.views import APIView
from rest_framework import generics, mixins, viewsets
from rest_framework.response import Response
from rest_framework import status
import time


class GetVerificationCodeView(APIView):
    def post(self, request):
        serializer = PhoneNumberSerializer(data=request.data)
        if serializer.is_valid():
            # Имитация отправки кода авторизации с задержкой
            time.sleep(2)
            return Response({"message": "Код авторизации отправлен"})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):
    def post(self, request):
        serializer = VerificationSerializer(data=request.data)
        if serializer.is_valid():
            user, created = CustomUser.objects.get_or_create(phone_number=serializer.data.get('phone_number'))
            if created:
                user.invite_code = ''.join(secrets.choice(string.ascii_letters + string.digits) for _ in range(6))
                user.save()

            login(request, user)
            token = RefreshToken.for_user(user)
            return Response({"access": str(token.access_token)})

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UsersListView(generics.ListAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer


class UserProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)

    def patch(self, request):
        code = request.data.get('code')
        user = request.user

        if user.invited_by:
            return Response(status=status.HTTP_400_BAD_REQUEST, data={"message": "Код уже был введён"})

        if code == user.invite_code:
            return Response(status=status.HTTP_400_BAD_REQUEST, data={"message": "Вы не можете ввести свой код"})

        if CustomUser.objects.get(invite_code=code):
            user.invited_by = code
            user.save()
            return Response(status=status.HTTP_200_OK, data={"message": "Код успешно введён"})

        return Response(status=status.HTTP_400_BAD_REQUEST, data={"message": "Код не существует"})




