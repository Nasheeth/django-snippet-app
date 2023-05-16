from django.urls import path
from .views import (
    SnippetOverviewAPI,
    SnippetCreateAPI,
    SnippetDetailAPI,
    SnippetUpdateAPI,
    SnippetDeleteAPI,
    TagListAPI,
    TagDetailAPI,
)

urlpatterns = [
    path('overview/', SnippetOverviewAPI.as_view(), name='snippet-overview'),
    path('create/', SnippetCreateAPI.as_view(), name='snippet-create'),
    path('detail/<int:pk>/', SnippetDetailAPI.as_view(), name='snippet-detail'),
    path('update/<int:pk>/', SnippetUpdateAPI.as_view(), name='snippet-update'),
    path('delete/<int:pk>/', SnippetDeleteAPI.as_view(), name='snippet-delete'),
    path('tags/', TagListAPI.as_view(), name='tag-list'),
    path('tags/<int:pk>/', TagDetailAPI.as_view(), name='tag-detail'),
]
