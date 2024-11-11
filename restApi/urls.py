from django.urls import path

from restApi import views

urlpatterns = [
    path('get', views.get_transaction, name='get_transaction'),
    path('process', views.process_transaction, name='process_transaction'),
    path('process_v2', views.process_V2_transaction, name='process_V2_transaction'),
]