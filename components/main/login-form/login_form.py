from django_components import component


@component.register("login-form")
class LoginForm(component.Component):
    template_name = "main/login-form/login-form.html"

    def get_context_data(self, form):
        return {
            "form": form,
        }

    class Media:
        css = "main/login-form/login-form.css"
