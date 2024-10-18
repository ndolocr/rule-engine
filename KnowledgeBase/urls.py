from django.urls import path

from KnowledgeBase import views

urlpatterns = [
    path('get/rules/by/namespace/<str:namespace>', views.getRuleByNamespace, name='get_by_namespace'),
]