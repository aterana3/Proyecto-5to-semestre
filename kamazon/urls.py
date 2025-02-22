"""
URL configuration for kamazon project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from apps.core.views import home
from apps.core.views import training
from django.urls import include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home.HomeView.as_view(), name='home'),
    path('training', training.TrainingBuildView.as_view(), name='training'),
    path('auth/', include('apps.authentication.urls')),
    path('settings/', include('apps.settings.urls')),
    path('products/', include('apps.products.urls')),
    path('shopping-cart/', include('apps.shopping_cart.urls')),
    path('billing/', include('apps.billing.urls')),
    path("ckeditor5/", include('django_ckeditor_5.urls'), name='ck_editor_5_upload_file'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)