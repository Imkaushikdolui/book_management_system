from django.utils import timezone
from rest_framework import generics
from apiauth.models import Account
from .serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import get_user_model

from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import get_user_model
from rest_framework.exceptions import AuthenticationFailed
import jwt
import datetime
from rest_framework import status

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

# JWT authentication
class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['username'] = user.username    
        token['email'] = user.email    
        return token

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

User = get_user_model()

class AccountLoginAPI(APIView):

    def post(self, request, *args, **kwargs):
        email = request.data['email']
        username = request.data['username']
        password = request.data['password']

        user = User.objects.filter(username=username).first()

        if user is None:
            raise AuthenticationFailed("User not found")

        if not user.check_password(password):
            raise AuthenticationFailed("Incorrect password")

        payload = {
            'id': user.id,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
            'iat': datetime.datetime.utcnow()
        }

        token = jwt.encode(payload, 'secret', algorithm='HS256')

        response = Response()

        # httponly = true //becuase we dont want frontend to acess the token,its for the backend only
        response.set_cookie(key='jwt', value=token, httponly=True)

        response.data = {
            "jwt": token,
        }

        return response


account_login_view = AccountLoginAPI.as_view()


class UserJWTView(APIView):

    def get(self, request):
        token = request.COOKIES.get('jwt')

        if not token:
            raise AuthenticationFailed("UnAuthenticated!!")

        try:
            payload = jwt.decode(token, 'secret', algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed("Token has expired")
        except jwt.DecodeError:
            raise AuthenticationFailed("Token is invalid")

        # Use single quotes around 'id' to access the key
        user_id = payload['id']
        user = User.objects.get(id=user_id)
        serializer = AccountSerializer(user)
        return Response(serializer.data)


user_jwt_view = UserJWTView.as_view()


class AccountLogoutAPI(APIView):
    def post(self, request):

        response = Response({"message": "Logged out successfully"})

        # Delete the 'jwt' cookie by setting its value to an empty string and setting its expiration time to a past date
        response.delete_cookie('jwt')

        return response


account_logout_view = AccountLogoutAPI.as_view()

# ACCOUNT REGISTER APIViews


class AccountRegisterAPI(APIView):
    def post(self, request, *args, **kwargs):
        try:
            data = request.data
            serializer = AccountSerializer(data=data)
            if serializer.is_valid():
                email = serializer.validated_data.get('email')
                if Account.objects.filter(email=email).exists():
                    return Response({
                        'status': 400,
                        'message': 'Email already registered',
                        'data': 'Try to register with a different email or try logging in'
                    })
                serializer.save()
                return Response({
                    'status': 201,  # Created
                    'message': 'Account created successfully',
                    'data': serializer.data
                }, status=201)

            return Response({
                'status': 400,
                'message': 'Registration failed. Something went wrong!!',
                'data': serializer.errors,
            }, status=400)
        except Exception as e:
            print(e)  # Print error for debugging
            return Response({
                'status': 500,  # Internal Server Error
                'message': 'Internal Server Error. Please try again later.',
            }, status=500)


account_register_view = AccountRegisterAPI.as_view()


class AccountListAPIView(generics.ListAPIView):
    serializer_class = AccountSerializer

    def get_queryset(self):
        # Filter the queryset to retrieve all accounts
        queryset = Account.objects.all()
        return queryset


account_list_view = AccountListAPIView.as_view()


class AccountDetailAPIView(generics.RetrieveAPIView):

    queryset = Account.objects.all()
    serializer_class = AccountDetailSerializer


account_detail_view = AccountDetailAPIView.as_view()


class AccountUpdateAPIView(generics.UpdateAPIView):

    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    lookup_field = 'pk'

    def perform_update(self, serializer):
        serializer.save()

    def update(self, request, *args, **kwargs):
        response = super().update(request, *args, **kwargs)
        
        if response.status_code == status.HTTP_200_OK: 
            account_updated_data= response.data
            response_data = {
                'status': status.HTTP_200_OK,
                'message': 'Account updated successfully!',
                'data': account_updated_data
            }
            return Response(response_data, status=status.HTTP_200_OK)
        else:
            return response

account_update_view = AccountUpdateAPIView.as_view()


class AccountDestroyAPIView(generics.DestroyAPIView):

    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    lookup_field = 'pk'

    def perform_destroy(self, instance):
        instance.delete()

    def delete(self, request, *args, **kwargs):
        response = super().delete(request, *args, **kwargs)
        
        if response.status_code == status.HTTP_204_NO_CONTENT:
            response_data = {
                'status': status.HTTP_204_NO_CONTENT,
                'message': 'Account deleted successfully!',
            }
            return Response(response_data, status=status.HTTP_204_NO_CONTENT)
        else:
            return response

account_destroy_view = AccountDestroyAPIView.as_view()
