# from oscar.views.decorators import login_forbidden
from oscar.apps.catalogue.models import Product
from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = 'oscar/layout.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['products'] = Product.objects.filter(is_public=True)
        return context
