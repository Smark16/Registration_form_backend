from rest_framework import serializers
from .models import *
from rest_framework_simplejwt.tokens import Token
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username','is_staff', 'is_customer']

class userAcountSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAccounts
        fields = ["id", "user"]

class obtainSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['is_staff'] = user.is_staff
        token['username'] = user.username
        token['email'] = user.email 

        return token


class PersonalSerializer(serializers.ModelSerializer):
    class Meta:
        model= PersonalInfomation
        fields =  ["id", "Admission_No", "Surname", "Other_Names", "Sex", "Date_Of_Birth", "Age", "Postal_Address", "Telephone", "Email", "Home_District", "Subcounty", "Nationality", "Occupation", "Present_Job_TiTle"]
    
class EmployerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employer
        fields =  ["id", "Employer", "Postal_Address","Telephone", "Email"]