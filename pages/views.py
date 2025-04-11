from django.views.generic import TemplateView
from django.shortcuts import render
from oscar.apps.catalogue.models import Product, Category
from django.db.models import Count


class HomeView(TemplateView):
    template_name = 'oscar/index.html'
    model = Category
    context_object_name = 'categories'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['products'] = Product.objects.filter(is_public=True)
        context['categories'] = Category.objects.annotate(product_count=Count('product'))
        return context


def about_view(request):
    return render(request, 'oscar/about.html')


def custom_page_not_found(request, exception):
    return render(request, 'oscar/404.html', status=404)
