from django.urls import path

from .views import SongListView, IndexView, SongLikeView

app_name = "core"

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('songs/', SongListView.as_view(), name='songs'),
    path('song/like/<int:pk>/', SongLikeView.as_view(), name='song-like'),
]
