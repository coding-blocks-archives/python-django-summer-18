from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('login/', views.login_view, name = 'login'),
    path('logout/', views.logout_view, name = 'logout'),
    path('restaurants/', views.restaurants, name = 'restaurants'),
    path('addRestaurants/', views.add_restraunt, name = 'addRestaurants'),
    path('restaurant/<int:pk>', views.RestaurantView.as_view(), name = 'restaurant'),
    path('review/<int:id>', views.review, name = 'review')
]