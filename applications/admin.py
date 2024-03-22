from django.contrib import admin
from .models import *

# Register your models here.
class PersonAdmin(admin.ModelAdmin):
    list_display = ["id", "Admission_No", "Surname", "Other_Names", "Sex", "Date_Of_Birth", "Age", "Postal_Address", "Telephone", "Email", "Home_District", "Subcounty", "Nationality", "Occupation", "Present_Job_TiTle"]

class EmployAdmin(admin.ModelAdmin):
    list_display = ["id", "Employer", "Postal_Address","Telephone", "Email"]

class AccountAdmin(admin.ModelAdmin):
    list_display = ["id", "user"]


admin.site.register(PersonalInfomation, PersonAdmin)
admin.site.register(Employer, EmployAdmin)
admin.site.register(UserAccounts, AccountAdmin)
