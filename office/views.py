# from oscar.views.decorators import login_forbidden
from django.views.generic import TemplateView, DetailView
from oscar.apps.catalogue.models import Product, Category


class HomeView(TemplateView):
    template_name = 'oscar/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['products'] = Product.objects.filter(is_public=True).select_related('category')
        return context


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
