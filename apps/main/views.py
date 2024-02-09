from django.conf import settings
from django.contrib.auth import logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView as DjangoLoginView
from django.shortcuts import redirect
from django.views.generic import TemplateView


class MainView(TemplateView):
    template_name = "main/index.html"

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect(settings.DEFAULT_APP_URL_NAME)
        return super().get(request, *args, **kwargs)


class LoginView(DjangoLoginView):
    template_name = "main/login.html"
    form_class = AuthenticationForm

    def dispatch(self, request, *args, **kwargs):
        logout(request)
        return super().dispatch(request, *args, **kwargs)
