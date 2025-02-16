from django.urls import path
from .views import home, add_to_cart, view_cart
from django.contrib.auth.views import LoginView, LogoutView
from .views import custom_register, custom_login, logout
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', home, name='home'),
    path('cart/', view_cart, name='cart'),
    path('add-to-cart/<int:product_id>/', add_to_cart, name='add_to_cart'),
    path('register/', custom_register, name='register'),
    path('login/', custom_login, name='login'),
    path('logout/', logout, name='logout'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)