from djongo import models

# Create your models here.

class Video(models.Model):
    title = models.CharField(max_length=60)
    desc = models.TextField()
    channel = models.CharField(max_length=30)
    image = models.ImageField(blank=False)
    video = models.FileField(blank=False)
    views = models.IntegerField(null=True)
    time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return (self.title)