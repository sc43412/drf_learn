# from django.shortcuts import render
# from functools import partial
from rest_framework.views import APIView
from rest_framework.views import Response
from rest_framework.decorators import api_view
from api.serializers import StudentSeralizer
from api.models import Student
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated


# Create your views here.
@api_view(['GET','POST','PUT'])
def get_data(request):
     print(request.method)
     if request.method=='GET':
       return Response({"message": "Hello, world!"})
     if request.method=='POST':
         print(request.data)
         serl= StudentSeralizer(data=request.data)
         if serl.is_valid():
              serl.save()
              return Response({"message": "data is saved"})
         else:
             return Response({"msg":"wrong information validation"},status=400)
     if request.method=='PUT':
         print(request.data)
         if not request.data.get('id'):
             return Response({"msg":"wrong information validation"},status=400)
         qs = Student.objects.get(id=request.data['id'])
         serl= StudentSeralizer(qs,data=request.data,partial=True)
         if serl.is_valid():
              serl.save()
              return Response({"message": "data is saved"})
         else:
             print(serl.error_messages)
             return Response({"msg":"wrong information validation"},status=400)  
         
class ListViews(APIView):
    # authentication_classes=[BasicAuthentication]
    # permission_classes=[IsAuthenticated]
    def post(self,request):
         print(request.data)
         serl= StudentSeralizer(data=request.data)
         if serl.is_valid():
              serl.save()
              return Response({"message": "data is saved"})
         else:
             return Response({"msg":"wrong information validation"},status=400)    
    def get(self,request):
        qs = Student.objects.all()
        src = StudentSeralizer(qs,many=True)
        return Response({"data" : src.data},status=200)  
    def put(self,request):
         if not request.data.get('id'):
             return Response({"msg":"wrong information validation"},status=400)
         qs = Student.objects.get(id=request.data['id'])
         serl= StudentSeralizer(qs,data=request.data,partial=True)
         if serl.is_valid():
              serl.save()
              return Response({"message": "data is saved"})
         else:
             print(serl.error_messages)
             return Response({"msg":"wrong information validation"},status=400)  




