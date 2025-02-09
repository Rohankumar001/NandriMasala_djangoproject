from django.contrib import admin
from django.urls import path
from ecom import views
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from django.contrib.auth import views as auth_views
from ecom.forms import CustomPasswordResetForm



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home_view, name='home'),  # Corrected empty string to 'home'
    path('afterlogin', views.afterlogin_view, name='afterlogin'),
    
    path('logout', views.userlogout, name='logout'),

    path('aboutus', views.aboutus_view, name='aboutus'),
    path('contactus', views.contactus_view, name='contactus'),
    path('search', views.search_view, name='search'),
    path('send-feedback', views.send_feedback_view, name='send-feedback'),
    path('view-feedback', views.view_feedback_view, name='view-feedback'),

    path('adminclick', views.adminclick_view, name='adminclick'),
    path('adminlogin', LoginView.as_view(template_name='ecom/adminlogin.html'), name='adminlogin'),
    path('admin-dashboard', views.admin_dashboard_view, name='admin-dashboard'),

    path('view-customer', views.view_customer_view, name='view-customer'),
    path('delete-customer/<int:pk>', views.delete_customer_view, name='delete-customer'),
    path('update-customer/<int:pk>', views.update_customer_view, name='update-customer'),

    path('admin-products', views.admin_products_view, name='admin-products'),
    path('admin-restock', views.admin_restock_view, name='admin-restock'),
    path('admin-add-product', views.admin_add_product_view, name='admin-add-product'),
    path('delete-product/<int:pk>', views.delete_product_view, name='delete-product'),
    path('update-product/<int:pk>', views.update_product_view, name='update-product'),
    path('update-product-edit-stock/<int:pk>', views.update_product_edit_stock, name='update-product-edit-stock'),


    path('admin-view-booking', views.admin_view_booking_view, name='admin-view-booking'),
    path('delete-order/<int:pk>', views.delete_order_view, name='delete-order'),
    path('update-order/<int:pk>', views.update_order_view, name='update-order'),

    path('customersignup', views.customer_signup_view, name='customersignup'),
    path('customerlogin', LoginView.as_view(template_name='ecom/customerlogin.html'), name='customerlogin'),
    path('customer-home', views.customer_home_view, name='customer-home'),
    path('my-order', views.my_order_view, name='my-order'),
    path('my-profile', views.my_profile_view, name='my-profile'),
    path('edit-profile', views.edit_profile_view, name='edit-profile'),
    path('download-invoice/<int:orderID>/<int:productID>', views.download_invoice_view, name='download-invoice'),

    path('add-to-cart/<int:pk>', views.add_to_cart_view, name='add-to-cart'),
    path('cart', views.cart_view, name='cart'),
    # path('cart/<int:id>', views.nncart_view, name='cart'),
    path('remove-from-cart/<int:pk>', views.remove_from_cart_view, name='remove-from-cart'),
    path('customer-address', views.customer_address_view, name='customer-address'),
    path('payment-success', views.payment_success_view, name='payment-success'),
    path('shop/<int:pk>', views.shop_view, name='shop'),
    path('decreace_quntity/<int:id>', views.decreace_quntity, name='decreace_quntity'),
    path('increace_quntity/<int:id>', views.increace_quntity, name='increace_quntity'),

   path('decreace_quntity/<int:id>', views.decreace_quntity, name='decreace_quntity'),
path('increace_quntity/<int:id>', views.increace_quntity, name='increace_quntity'),
    
]
