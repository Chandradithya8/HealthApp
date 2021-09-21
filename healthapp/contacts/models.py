from django.db import models
from django.utils import timezone
# Create your models here.


class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    message = models.TextField()
    created_date = models.DateTimeField(default=timezone.now, blank=True)

    def __str__(self):
        return self.name
