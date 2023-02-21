from django.urls import path
from . import views

urlpatterns = [
    path("<int:number>/", views.GetFibonnaciAPIView.as_view(), name="fibonacci"),
]
