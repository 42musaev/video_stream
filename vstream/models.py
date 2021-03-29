from django.db import models


class Video(models.Model):
    name = models.CharField(max_length=1024, blank=True)
    video = models.FileField(unique='videos')

    def __str__(self):
        if self.name:
            return self.name
        return self.video.name

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
