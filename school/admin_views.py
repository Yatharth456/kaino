from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import *
from .serializers import SchoolSerializer, SessionSerializer, LessionSerializer
from .decorators import my_admin_decorator
from django.utils.decorators import method_decorator
from rest_framework import status

class CreateSchoolView(APIView):
    permission_classes = [IsAuthenticated]

    @method_decorator(my_admin_decorator)
    def post(self, request):
        data = request.data
        serializer = SchoolSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response({"msg": "School created.", "data": serializer.data})
    
class TermSystem(APIView):
    permission_classes = [IsAuthenticated]

    @method_decorator(my_admin_decorator)
    def post(self, request):
        data = request.data
        serializer = SessionSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response({"msg": "Session created.", "data": serializer.data})
    
class CreateLession(APIView):
    permission_classes = [IsAuthenticated]

    @method_decorator(my_admin_decorator)
    def post(self, request):
        data = request.data
        serializer = LessionSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response(serializer.data)
    
class ChangeRole(APIView):
    permission_classes = [IsAuthenticated]

    @method_decorator(my_admin_decorator)
    def post(self, request):
        data = request.data
        try:
            user = User.objects.get(id=data['id'])
            user.role = data['role']
            user.save()
            return Response({"msg": "Role changed."})
        except:
            return Response({"msg": "Please provide id and role."})