from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from . import views

urlpatterns = [
    # path('', csrf_exempt(views.ListProject.as_view())),
    path('project', views.ListProject.as_view()),
    path('student', views.ListStudent.as_view()),
    # path('<int:pk>/', csrf_exempt(views.DetailProject.as_view())),
    path('<int:pk>/project', views.DetailProject.as_view()),
    path('<int:pk>/student', views.DetailStudent.as_view()),
]
