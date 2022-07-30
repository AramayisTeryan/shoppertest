from django.urls import path
from . import views

urlpatterns=[
    path('', views.HomeListView.as_view(), name='home'),
    path('product/', views.ProdListView.as_view(), name='product'),
    path('product_detail/<int:id>/', views.ProdDetailView.as_view(), name='product_detail'),
    path('cart/', views.CartListView.as_view(), name='cart'),
    path('blog/', views.BlogListView.as_view(), name='blog'),
    path('blogsingle/', views.BlogSingleListView.as_view(), name='blogsingle'),
    path('404/', views.ErrorListView.as_view(), name='404'),
    path('contact/', views.ContactListView.as_view(), name='contact'),
    path('register/', views.register_request, name='register'),
    path('login/', views.login_request, name='login'),
    path('logout', views.logout_request, name = 'logout'),
    path("add-to-cart", views.add_to_cart, name="add-to-cart"),
    path("cart_quantity_update", views.cart_quantity_update, name="cart_quantity_update"),
    path("cart_quantity_delete", views.cart_quantity_delete, name="cart_quantity_delete"),
    path("cart", views.cartview, name="cart"),
]