from django.urls import path

from . import views

# app_name = 'jira_url-json_to_issue'
urlpatterns = [
    path('', views.index, name='index'),
    path('IssueForm', views.get_name, name='get_name'),
    path('json/<json1>/', views.jsonn, name='json'),
]
