"""
URL configuration for office project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.apps import apps
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views
from .views import HomeView, about_view, contact_view
from django.contrib.flatpages import views as flatpages_views


urlpatterns = [
    path('i18n/', include('django.conf.urls.i18n')),
    path('', HomeView.as_view(), name='home'),  # Должен быть первым
    path('pages/', include('pages.urls')),
    path('', include(apps.get_app_config('oscar').urls[0])),
    path('admin/', admin.site.urls),
    path('catalogue/category/<slug:slug>_<int:pk>/', views.CategoryView.as_view(), name='category_view'),
    path('about', about_view, name='about'),
    path('contact', contact_view, name='contact'),
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


handler404 = 'pages.views.custom_page_not_found'
