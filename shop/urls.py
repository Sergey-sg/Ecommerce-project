from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('category/<slug:category_slug>/<slug:product_slug>', views.product, name='product_detail'),
    path('category/<slug:category_slug>', views.home, name='products_by_categories'),
    path('cart/', views.cart_detail, name='cart_detail'),
    path('cart/add/<int:product_id>/', views.add_cart, name='add_cart'),
    path('cart/remove/<int:product_id>/', views.cart_remove, name='cart_remove'),
    path('cart/remove_product/<int:product_id>/', views.cart_remove_product, name='cart_remove_product'),
    path('account/create/', views.signUpVievs, name='signup'),
    path('account/login/', views.loginViev, name='login'),
    path('account/signout/', views.singoutView, name='signout'),
]
