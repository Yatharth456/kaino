from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import *
from .serializers import TeacherSerializer, UserSerializer
from .decorators import my_teacher_decorator
from django.utils.decorators import method_decorator
from rest_framework import status

class TeacherProfileView(APIView):
    permission_classes = [IsAuthenticated]

    @method_decorator(my_teacher_decorator)
    def post(self, request):
        data = request.data
        data['teacher'] = request.user.id
        try:
            serializer = TeacherSerializer(data=data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response({"msg": "Updated.", "data": serializer.data})
        except:
            return Response({"msg": "Please provide valid qualification, date_of_joining and experience."})
        

class GetTeachers(APIView):
    def get(self, request):
        user = User.objects.filter(role=3)
        profile = Profile.objects.filter()
        serializer = TeacherSerializer(profile, many=True)
        serializer1 = UserSerializer(user, many=True)
        return Response({"profile": serializer.data, "teacher": serializer1.data}, status=200)


