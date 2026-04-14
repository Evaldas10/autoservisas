
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
    path("instances/", views.OrderInstanceListView.as_view(), name="instances"),
    path("instances/<int:pk>",
         views.OrderInstanceDetailView.as_view(), name="instance"),
    path('instances/create/', views.OrderInstanceCreateView.as_view(),
         name="instance_create"),
    path('instances/<int:pk>/update/',
         views.OrderInstanceUpdateView.as_view(), name="instance_update"),
    path('instances/<int:pk>/delete/',
         views.OrderInstanceDeleteView.as_view(), name="instance_delete"),
    path("orders/<int:pk>/add-line/",
         views.OrdrLineCreateView.as_view(), name="orderLine_create"),
    path("ordersLines/<int:pk>/", views.OrderLineUpdateView.as_view(),
         name="orderLine_update"),
    path("register-car/", views.register_car, name="register_car"),
    path('ajax/load-models/', views.load_models, name='ajax_load_models'),
]
