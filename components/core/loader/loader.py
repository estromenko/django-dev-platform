from django_components import component


@component.register("loader")
class Loader(component.Component):
    template_name = "core/loader/loader.html"

    def get_context_data(self, element_id=None):
        return {
            "element_id": element_id,
        }

    class Media:
        css = "core/loader/loader.css"
