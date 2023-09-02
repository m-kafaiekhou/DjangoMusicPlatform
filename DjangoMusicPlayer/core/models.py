from django.db import models
from django.template.defaultfilters import slugify

# Local imports
from .utils import song_path
from accounts.models import CustomUser

# Models


class Genre(models.Model):
    name = models.CharField(max_length=50)
    thumbnail = models.ImageField(upload_to="genres", default="genres/default.png")

    def __str__(self):
        return self.name


class Artist(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    image = models.ImageField(upload_to="artists", default="artists/default.png")
    bio = models.TextField(verbose_name='Artist Bio', null=True, blank=False)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Artist, self).save(*args, **kwargs)


class Song(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, verbose_name="Song name")
    description = models.TextField()
    thumbnail = models.ImageField(upload_to="thumbnails", blank=False)
    song = models.FileField(upload_to=song_path, max_length=500)
    genre = models.ForeignKey(Genre, on_delete=models.DO_NOTHING)
    artists = models.ManyToManyField(Artist, related_name='songs')
    created_at = models.DateTimeField(verbose_name='Created At', auto_now_add=True)

    def __str__(self):
        return self.title


class Playlist(models.Model):
    title = models.CharField(max_length=200, verbose_name="Title")
    description = models.TextField()
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    song = models.ManyToManyField(Song, related_name='playlists')


class Like(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    song = models.ForeignKey('Song', on_delete=models.CASCADE)
    like_date = models.DateTimeField(auto_now_add=True)


class Comment(models.Model):
    STATUS_CHOICES = (
        ('p', 'Pending'),
        ('a', 'Accept'),
        ('r', 'Reject'),
    )
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    song = models.ForeignKey('Song', on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)
    status = models.CharField(choices=STATUS_CHOICES, max_length=1)
