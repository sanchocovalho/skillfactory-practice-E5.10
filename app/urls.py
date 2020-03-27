from app import views
from django.urls import path
from django.conf.urls import handler404

app_name = 'app'
urlpatterns = [
    path('', views.CarList.as_view(), name='car-list'),
    path('create/', views.CarCreate.as_view(), name="car-create"),
    path("update<int:pk>/", views.CarUpdate.as_view(), name="car-update"),
    path("delete<int:pk>/", views.CarDelete.as_view(), name="car-delete"),
]

handler404 = 'app.views.error_404_view'
