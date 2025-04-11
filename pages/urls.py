from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import HomeView, about_view


urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('about', about_view, name='about'),
    ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
