from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.hashers import make_password, check_password
from rest_framework.permissions import IsAuthenticated
from .models import *
from .decorators import my_student_decorator
from django.utils.decorators import method_decorator



class StudentProfileView(APIView):
    permission_classes = (IsAuthenticated,)

    @method_decorator(my_student_decorator)
    def post(self, request):
        data = request.data
        student = get_object_or_404(User, id=request.user.id)
        try:
            if student is not None:
                student.first_name = data['first_name']
                student.last_name = data['last_name']
                student.gender = data['gender']
                student.dob = data['dob']
                student.mobile_no = data['mobile_no']
                student.address = data['address']
                student.zip_code = data['zip_code']
                student.profile_img = data['profile_img']
                student.save()
            return Response({"msg": "Profile Updated."})
        except:
            return Response({"msg": "Please provide valid first_name, last_name, gender, dob, mobile_no, address, zip_code and profile_img."})