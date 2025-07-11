# from oscar.views.decorators import login_forbidden
from django.views.generic import TemplateView, DetailView
from oscar.apps.catalogue.models import Category
from django.shortcuts import render
from django.db.models import Count
from oscar.core.loading import get_model
from django.contrib.flatpages.models import FlatPage
from django.shortcuts import get_object_or_404
from .models import CustomFlatPage


Product = get_model('catalogue', 'Product')
Category = get_model('catalogue', 'Category')


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

        # Получаем категорию по ID=3
        promo_category = Category.objects.get(id=3)
        promoted_products = Product.objects.filter(
            categories__in=promo_category.get_descendants_and_self(),
            is_public=True
        ).browsable().select_related('parent')[:8]  # Ограничение до 8 товаров
        new_products = Product.objects.filter(
            is_public=True
        ).order_by('-date_created').select_related('parent')[:8]
        context.update({
            'promoted_products': promoted_products,
            'new_products': new_products,
            'categories': Category.objects.annotate(
                product_count=Count('product')
            ).filter(depth=1)
        })
        return context


def about_view(request):
    flatpage = get_object_or_404(CustomFlatPage, url='/about/')  # Убедитесь, что URL совпадает с вашим
    return render(request, 'flatpages/about.html', {'flatpage': flatpage})


def contact_view(request):
    flatpage = get_object_or_404(FlatPage, url='/contact/')  # Убедитесь, что URL совпадает с вашим
    return render(request, 'flatpages/contact.html', {'flatpage': flatpage})


def custom_page_not_found(request, exception):
    return render(request, 'oscar/404.html', status=404)
