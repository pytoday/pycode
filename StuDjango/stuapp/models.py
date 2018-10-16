from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Topic(models.Model):
    """Study title"""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User)

    def __str__(self):
        return self.text


class Entry(models.Model):
    """Studied details about something."""
    topic = models.ForeignKey(Topic)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        """models returned formated by strings"""

        return self.text[:50] + "..."