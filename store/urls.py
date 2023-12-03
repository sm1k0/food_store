# store/urls.py
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import product_detail
from .views import custom_404

from .views import (
    home, category_detail, cart, add_to_cart, remove_from_cart,
    CustomLoginView, RegisterView, ProfileView, LogoutView, ProfileUpdateView
)
handler404 = custom_404
urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
    path('accounts/profile/', ProfileView.as_view(), name='profile'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('', home, name='home'),
    path('category/<int:category_id>/', category_detail, name='category_detail'),
    path('cart/', cart, name='cart'),
    path('add_to_cart/<int:product_id>/', add_to_cart, name='add_to_cart'),
    path('remove_from_cart/<int:order_id>/<int:product_id>/', remove_from_cart, name='remove_from_cart'),
    path('accounts/profile/update/', ProfileUpdateView.as_view(), name='profile_update'),
    path('product/<int:category_id>/<int:product_id>/', product_detail, name='product_detail'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
