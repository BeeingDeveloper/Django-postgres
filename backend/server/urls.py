from django.urls import path
from .views import UserListView, SongListView, UserDetailView

urlpatterns = [
    path('users/', UserListView.as_view(), name='user-list'),
    path('songs/', SongListView.as_view(), name='song-list'),
    path('users/<int:pk>/', UserDetailView.as_view(), name='user-detail')
]