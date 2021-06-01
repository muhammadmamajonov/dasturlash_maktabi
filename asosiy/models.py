from django.db import models

# Create your models here.

class Playlist(models.Model):
    nomi = models.CharField(max_length=100)
    rasm = models.ImageField(upload_to = 'rasmlar/playlist_rasm')
    sana = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.nomi


class VideoDars(models.Model):
    nomi = models.CharField(max_length=100)
    rasm = models.ImageField(upload_to = 'video_daraslar/rasmlar')
    izox = models.TextField()
    video = models.FileField(upload_to='video_darslar/video')
    playlisti = models.ForeignKey(Playlist, on_delete=models.CASCADE)
    # sana = models.DateField(auto_now_add=True)

    