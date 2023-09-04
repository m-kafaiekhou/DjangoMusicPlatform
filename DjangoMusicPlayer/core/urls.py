from django.urls import path

from .views import SongListView, IndexView

app_name = "core"

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('songs/', SongListView.as_view(), name='songs'),
]
