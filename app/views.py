from django.shortcuts import render
from django.http import HttpResponse
# from rest_framework import generics
from rest_framework.views import APIView
from . models import *
from . serializer import *
from rest_framework.response import Response

# Create your views here.

def Main(request):
    return HttpResponse("Hello")




# ********************
# class ReactView(APIView):

#     serializer_class = ReactSerializer

#     def get(self, request):
#         output = [{"employee": output.employee, "department": output.department}
#                   for output in React.objects.all()]
#         return Response(output)

#     def post(self, request):

#         serializer = ReactSerializer(data=request.data)
#         if serializer.is_valid(raise_exception=True):
#             serializer.save()
#             return Response(serializer.data)

# # class ReactView(generics.ListCreateAPIView):
# #     queryset = React.objects.all()
# #     serializer_class = ReactSerializer


