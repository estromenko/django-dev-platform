from django.urls import path

from apps.main import views

urlpatterns = [
    path("", views.MainView.as_view(), name="main"),
    path("login/", views.LoginView.as_view(), name="login"),
]
