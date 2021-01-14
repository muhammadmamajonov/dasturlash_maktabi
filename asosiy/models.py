from django.db import models

# Create your models here.

class Playlist(models.Model):
    nomi = models.CharField(max_length=100)
    rasm = models.ImageField(upload_to = 'rasmlar/playlist_rasm')
    sana = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.nomi

    