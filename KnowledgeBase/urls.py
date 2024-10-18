from django.urls import path

from KnowledgeBase import views

urlpatterns = [
    path('get/by/namespace', view.getRuleByNamespace, name='get_by_namespace'),
]