from django.db import models
from django.contrib.auth.models import User


class Ticket(models.Model):
    class Status(models.TextChoices):
        STATUS_CLOSED = 'closed'
        STATUS_OPEN = 'open'
    title = models.CharField(max_length=100, blank=True)
    comment = models.TextField(default='')
    owner = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    answer = models.TextField()
    status = models.CharField(max_length=10, choices=Status.choices, default='open')

    class Meta:
        ordering = ['-created']
