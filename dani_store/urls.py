from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path, include
from .views import login_view, logout_view, register
from products import views


urlpatterns = [
    path('', views.ProductListView.as_view(), name='index'),
    path('admin/', admin.site.urls),
    path('carrito/', include('carts.urls')),
    path('productos/', include('products.urls')),
    path('usuarios/login', login_view, name='login'),
    path('usuarios/logout', logout_view, name='logout'),
    path('usuarios/register', register, name='register'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )
