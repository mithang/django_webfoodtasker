from django.urls import path, include
from django.contrib import admin
from django.contrib.auth.views import auth_login,auth_logout
from django.conf.urls.static import static
from django.conf import settings
from foodtaskerapp import views, apis

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    # path('restaurant/sign-in/', auth_login,
    #     {'template_name': 'restauant/sign_in.html'},
    #     name = 'restaurant-sign-in'),
    # path('restaurant/sign-out/', auth_logout,
    #     {'next_page': '/'},
    #     name = 'restaurant-sign-out'),
    path('restaurant/sign-in/', views.restaurant_login,
        name = 'restaurant-sign-in'),
    path('restaurant/sign-out/', auth_logout,
        name = 'restaurant-sign-out'),
    path('restaurant/sign-up', views.restaurant_sign_up,
        name = 'restaurant-sign-up'),
    path('restaurant/', views.restaurant_home, name = 'restaurant-home'),

    path('restaurant/account/', views.restaurant_account, name = 'restaurant-account'),
    path('restaurant/meal/', views.restaurant_meal, name = 'restaurant-meal'),
    path('restaurant/meal/add/', views.restaurant_add_meal, name = 'restaurant-add-meal'),
    path('restaurant/meal/edit/(?P<meal_id>\d+)/', views.restaurant_edit_meal, name = 'restaurant-edit-meal'),
    path('restaurant/order/', views.restaurant_order, name = 'restaurant-order'),
    path('restaurant/report/', views.restaurant_report, name = 'restaurant-report'),
    # Tu cai moi
    path('o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    # Sign In/ Sign Up/ Sign Out
    path('api/social/', include('rest_framework_social_oauth2.urls')),
    # /convert-token (sign in/ sign up)
    # /revoke-token (sign out)
    path('api/restaurant/order/notification/(?P<last_request_time>.+)/', apis.restaurant_order_notification),
    # APIs for CUSTOMERS
    path('api/customer/restaurants/', apis.customer_get_restaurants),
    path('api/customer/meals/(?P<restaurant_id>\d+)/', apis.customer_get_meals),
    path('api/customer/order/add/', apis.customer_add_order),
    path('api/customer/order/latest/', apis.customer_get_latest_order),
    path('api/customer/driver/location/', apis.customer_driver_location),

    # APIs for DRIVERS
    path('api/driver/orders/ready/', apis.driver_get_ready_orders),
    path('api/driver/order/pick/', apis.driver_pick_order),
    path('api/driver/order/latest/', apis.driver_get_latest_order),
    path('api/driver/order/complete/', apis.driver_complete_order),
    path('api/driver/revenue/', apis.driver_get_revenue),
    path('api/driver/location/update/', apis.driver_update_location),

    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
