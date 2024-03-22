from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import generics
from .models import *
from rest_framework.views import APIView
from .serializer import *
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import *
from rest_framework import status
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets

#from django.contrib.auth.decorators import login_required
#from django.contrib.auth import update_session_auth_hash
#from django.core.mail import send_mail
#from django.shortcuts import get_object_or_404

# Create your views here.
class ObtainPairView(TokenObtainPairView):
    serializer_class = obtainSerializer

class PersonalList(generics.ListAPIView):
    queryset = PersonalInfomation.objects.all()
    serializer_class = PersonalSerializer

class SinglePerson(generics.RetrieveAPIView):
    queryset = PersonalInfomation.objects.all()
    serializer_class = PersonalSerializer

    def retrieve(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            serializer = self.get_serializer(instance)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except PersonalList.DoesNotExist:
            return Response({'detail': 'Person Does Not Exist'}, status=status.HTTP_404_NOT_FOUND)


class EmployerList(generics.ListAPIView):
    queryset = Employer.objects.all()
    serializer_class = EmployerSerializer

class Single_employer(generics.RetrieveAPIView):
    queryset = Employer.objects.all()
    serializer_class = EmployerSerializer

    def retrieve(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            serializer = self.get_serializer(instance)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except EmployerList.DoesNotExist:
            return Response({'detail': 'Employer Does Not Exist'}, status=status.HTTP_404_NOT_FOUND)

class newPersonal(generics.CreateAPIView):
    serializer_class = PersonalSerializer
    permission_classes = [AllowAny]

    def post(self, request, format=None):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
class new_Employer(generics.CreateAPIView):
    serializer_class = EmployerSerializer
    permission_classes = [AllowAny]

    def post(self, request, format=None):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
class DeletePerson(generics.RetrieveDestroyAPIView):
      queryset = PersonalInfomation.objects.all()
      serializer_class = PersonalSerializer

      permission_classes = [AllowAny]

      def delete(self, request, *kwargs, **args):
          instance = self.get_object()
          instance.delete()

          return Response(status=status.HTTP_200_OK)
          
class EditPerson(generics.UpdateAPIView):
     queryset = PersonalInfomation.objects.all()
     serializer_class = PersonalSerializer

     permission_classes = [AllowAny]

     def update(self, request, *args, **kwargs):
         instance = self.get_object()
         serializer = self.serializer_class(instance, data=request.data)
         serializer.is_valid(raise_exception=True)
         serializer.save()

         return Response(serializer.data, status=status.HTTP_201_CREATED)
    
class DeleteEmployer(generics.RetrieveDestroyAPIView):
      queryset = Employer.objects.all()
      serializer_class = EmployerSerializer

      permission_classes = [AllowAny]

      def delete(self, request, *kwargs, **args):
          instance = self.get_object()
          instance.delete()

          return Response(status=status.HTTP_200_OK)
          
class EditEmployer(generics.UpdateAPIView):
     queryset = Employer.objects.all()
     serializer_class = EmployerSerializer

     permission_classes = [AllowAny]

     def update(self, request, *args, **kwargs):
         instance = self.get_object()
         serializer = self.serializer_class(instance, data=request.data)
         serializer.is_valid(raise_exception=True)
         serializer.save()

         return Response(serializer.data, status=status.HTTP_201_CREATED)
