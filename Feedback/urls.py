from django.urls import path
from . import views

app_name = 'Feedback'

urlpatterns = [
    path('escrever_feedback/', views.ver_feedback, name="ver_feedback"),
]