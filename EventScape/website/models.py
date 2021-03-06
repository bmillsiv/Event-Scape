from django.db import models
from django.contrib.auth.models import User

CHARFIELD_MAX_LENGTH = 255
APPROVED_CHOICES = (
    ('A', 'approved'),
    ('P', 'pending'),
    ('R', 'rejected')
)


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    follows = models.ManyToManyField('self', related_name='followed_by', symmetrical=False)


class Event(models.Model):
    host = models.ForeignKey(User)
    name = models.CharField(max_length=CHARFIELD_MAX_LENGTH)
    address = models.CharField(max_length=CHARFIELD_MAX_LENGTH)
    city = models.CharField(max_length=CHARFIELD_MAX_LENGTH)
    state = models.CharField(max_length=2)
    start = models.DateTimeField()
    end = models.DateTimeField(null=True, blank=True)
    description = models.TextField()
    approved = models.CharField(max_length=1, choices=APPROVED_CHOICES, default='P')
    attendees = models.ManyToManyField(User)


class EventImage(models.Model):
    event = models.ForeignKey(Event, related_name='images')
    image = models.ImageField()


class Tag(models.Model):
    name = models.CharField(max_length=CHARFIELD_MAX_LENGTH)
    approved = models.CharField(max_length=1, choices=APPROVED_CHOICES, default='P')
    users = models.ManyToManyField(User)
    events = models.ManyToManyField(Event)