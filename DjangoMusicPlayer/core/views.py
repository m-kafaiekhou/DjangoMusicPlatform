from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.views import generic

from .serializers import SongSerializer
from .models import Song


class SongListView(APIView):
    serializer_class = SongSerializer

    def get(self, request, *args, **kwargs):
        songs = Song.objects.all()
        if songs:
            serializer = SongSerializer(Song.objects.all(), many=True)
            return Response(serializer.data)
        else:
            return Response({})


class IndexView(generic.TemplateView):
    template_name = 'core/index.html'
