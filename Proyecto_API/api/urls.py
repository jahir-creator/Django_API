from django.urls import path
from .views import CompanyView

urlpatterns = [
    path('users/', CompanyView.as_view(), name='users_list'),
    path('users/<int:id>', CompanyView.as_view(), name='users_process')
]
