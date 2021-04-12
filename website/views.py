from django.views.generic import TemplateView


class indexview(TemplateView):
    template_name = "index.html"

    def get_context_data(self):
        ctxt = super().get_context_data()
        ctxt["username"] = "太郎"
        return ctxt


class aboutview(TemplateView):
    template_name = "about.html"

    def get_context_data(self):
        ctxt = super().get_context_data()
        ctxt["num_services"] = 13000
        ctxt["skills"] = [
            "C++",
            "Java",
            "C#",
            "Ruby",
            "Python",
        ]
        return ctxt
