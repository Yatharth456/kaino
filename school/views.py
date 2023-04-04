from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UserSerializer
from rest_framework import permissions
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from .models import User
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.hashers import make_password, check_password


# Create your views here.


class RegisterAPI(APIView):
    def post(self, request):
        data = request.data
        serializer = UserSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response({"msg": "User registered."})
    

class LoginAPI(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        refresh = RefreshToken.for_user(user)
        
        data = {
            'id': user.id,
            'role': user.role,
            'email': user.email,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'remember_me': user.remember_me,
            'request_access': user.request_access,
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }
        return Response({**data}, status=200)


class RequestAccessAPI(APIView):
    permission_classes = (permissions.AllowAny,)

    def get(self, request):
        email = request.data['email']
        if email is None:
            return Response({"email": "This is required field."})
        user = User.objects.get(email=email)
        if user is not None:
            subject = 'welcome,'
            html_message = f'Hi {user.first_name + user.last_name}, plaese click on link to change password. <a href=http://{settings.IP}/user/change_pswd/?data={email}>CLICK HERE </a>'
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [email, ]
            send_mail(
                subject=subject,
                message='',
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[email],
                fail_silently=False,
                html_message=html_message
            )
            return Response({"msg": "Please check your email."})
        
    

class PasswordChange(APIView):
    def post(self, request):
        data = request.data
        print(request.GET.get('data'),"params")
        try:
            password = data['password']
            re_password = data['re_password']
            user = User.objects.get(email=request.GET.get('data'))
            if password == re_password:
                user.password = make_password(password)
                # user.save()
                return Response({"msg": "Password changed."})
            return Response({"msg": "Password mismatched."})
        except:
            return Response({"msg": "Please provide 'password' and 'repassword' field."})
