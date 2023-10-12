from django.urls import path
from .views import TeacherAPIView, TeacherDetailAPIView, StudentListCreateAPIView, StudentRetrieveAPIView

urlpatterns = [
    path('teach/', TeacherAPIView.as_view(), name="teachers"),
    path('teach/<int:pk>/', TeacherDetailAPIView.as_view(), name="teachers_detail"),
    path('students/', StudentListCreateAPIView.as_view(), name="student"),
    path('students/<int:pk>/', StudentRetrieveAPIView.as_view(), name="student")
]