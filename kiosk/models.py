from django.db import models

# Create your models here.


class Source(models.model):
    '''Video sources for download'''
    url = models.URLField()
    name = models.TextField(blank=True)
    add_time = models.DateTimeField(auto_now=True)
    update_time = models.DateTimeField(auto_now=True)
    downloaded = models.BooleanField(default=False)
    comments = models.TextField(blank=True)
    uuid = models.UUIDField()


class LiveSource(models.model):
    url = models.URLField()
    name = models.TextField(blank=True)
    add_time = models.DateTimeField(auto_now=True)
    update_time = models.DateTimeField(auto_now=True)
    comments = models.TextField(blank=True)
    uuid = models.UUIDField()


class FileEntry(models.model):
    path = models.TextField()
    source = models.ForeignKey('Source')


class Mode(models.model):
    FILE = 'file'
    LIVE = 'live'
    MODE_CHOICES = [
        (FILE, 'Play from file - play a downloaded video'),
        (LIVE, 'Play a live stream')
    ]
    mode = models.CharField(
        max_length=4,
        choices=MODE_CHOICES,
        default=FILE
    )
