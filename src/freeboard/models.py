from django.db import models
from django.utils import timezone

# Create your models here.

class FreeB(models.Model):
    user = models.ForeignKey('auth.User')
    title = models.CharField(max_length=150)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    view_count = models.IntegerField()

    def __str__(self):
        return "{} ({})".format(self.title, self.view_count)

class Comment(models.Model):
    fb_text = models.ForeignKey(FreeB)
    comment = models.CharField(max_length=200)
