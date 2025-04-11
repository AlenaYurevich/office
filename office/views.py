# from oscar.views.decorators import login_forbidden
from django.views.generic import TemplateView, DetailView
from oscar.apps.catalogue.models import Category, Product
from django.shortcuts import render
from django.db.models import Count


class CategoryView(DetailView):
    model = Category
    template_name = 'oscar/layout.html'
    context_object_name = 'category'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Add any additional context data if needed
        return context


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

