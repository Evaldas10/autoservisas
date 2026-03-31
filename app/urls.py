
from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path("about/", views.about, name='about'),
    path("cars/", views.cars, name="cars"),
    path("cars/<int:car_pk>/", views.car, name="car"),
    path("orders/", views.OrderListView.as_view(), name="orders"),
    path("orders/<int:pk>/", views.OrderDetailView.as_view(), name="order"),
    path("search/", views.search, name="search"),
    path("mycars/", views.MyCarInstanceListView.as_view(), name="mycars"),
    path("singup/", views.SingUp.as_view(), name="singup"),
    path('profile/', views.ProfileUpdateView.as_view(), name='profile'),
]
