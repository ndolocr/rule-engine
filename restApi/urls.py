from django.urls import path

from restApi import views

urlpatterns = [
    path('get', views.get_transaction, name='get_transaction'),
]