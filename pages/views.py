from oscar.apps.catalogue.models import Product
from django.views.generic import TemplateView
from django.shortcuts import render


class HomeView(TemplateView):
    template_name = 'oscar/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['products'] = Product.objects.filter(is_public=True)
        return context


def about_view(request):
    return render(request, 'oscar/about.html')


def custom_page_not_found(request, exception):
    return render(request, 'oscar/404.html', status=404)
