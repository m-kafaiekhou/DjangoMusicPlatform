from django.shortcuts import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from django.views import generic, View

from .serializers import SongSerializer
from .models import Song, Like
from .utils import APIAuthDecorator


class IndexView(generic.TemplateView):
    template_name = 'core/index.html'


class SongListView(APIView):
    serializer_class = SongSerializer

    @APIAuthDecorator
    def get(self, request, *args, **kwargs):
        songs = Song.objects.all()
        if songs:
            serializer = SongSerializer(Song.objects.all(), many=True)
            data = serializer.data.copy()

            for song in data:
                if Like.objects.filter(song_id=song['id'], user=request.user):
                    song['is_liked'] = 'true'
                else:
                    song['is_liked'] = 'false'
            return Response(data)
        else:
            return Response({})


class SongLikeView(View):
    def post(self, request, *args, **kwargs):
        delete = request.POST.get('del')
        print(delete)
        if delete == "true":
            Like.objects.get(song_id=kwargs['pk'], user=request.user).delete()
        else:
            Like.objects.create(song_id=kwargs['pk'], user=request.user)

        return HttpResponse(status=204)

class SongDetailView(generic.DetailView):
    template_name = 'core/song_details.html'
    model = Song

