from django.db import models
import datetime
from django.utils import timezone
from django.contrib.auth.models import User
from filebrowser.fields import FileBrowseField
from geoposition.fields import GeopositionField

# Create your models here.
class Observation(models.Model):
    species = models.CharField(max_length=200)
    common_name = models.CharField(max_length=200)
    curated = models.BooleanField()
    author = models.CharField(max_length=200)
    pub_date = models.DateTimeField('Date published', auto_now_add=True)
    edited_by  = models.ForeignKey(User, related_name='edited_by', blank=True, null=True, editable=False)
    edited_on  = models.DateTimeField('Date edited', auto_now=True, blank=True, null=True)
    OBSERVATION_TYPES = (
        ('Stationary', 'Stationary'),
        ('Traveling', 'Traveling'),
        ('Casual', 'Casual'),
        ('Area', 'Area'),
    )
    observation_type = models.CharField(max_length=20, choices=OBSERVATION_TYPES)
    location = models.CharField(max_length=200)
    gps = GeopositionField("GPS")
    image = FileBrowseField("Image", max_length=200, extensions=[".jpg",".png"], blank=True, null=True)
    description = models.TextField(max_length=500)
    revision_notes = models.TextField(max_length=500, blank=True, null=True)
    def __unicode__(self):  # Python 3: def __str__(self):
        return self.species
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'
