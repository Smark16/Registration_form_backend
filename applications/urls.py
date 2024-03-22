from django.urls import path
from . import views

urlpatterns = [
    path("", views.PersonalList.as_view()),
    path("employer", views.EmployerList.as_view()),
    path('new_person', views.newPersonal.as_view()),
    path('new_employer', views.new_Employer.as_view()),
    path('delete_person/<int:pk>', views.DeletePerson.as_view()),
    path("update_person/<int:pk>", views.EditPerson.as_view()),
    path('single_person/<int:pk>', views.SinglePerson.as_view()),

    path("delete_employer/<int:pk>", views.DeleteEmployer.as_view()),
    path("update_employer/<int:pk>", views.EditEmployer.as_view()),
    path('Single_employer/<int:pk>', views.Single_employer.as_view()),

    path('serializer', views.ObtainPairView.as_view()),
    
]
