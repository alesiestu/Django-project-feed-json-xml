from django.db import models
from django.utils import timezone

# Create your models here.

class Bill(models.Model):
      created_date = models.DateTimeField(default=timezone.now)
      value = models.FloatField()
 # cascata di valori da inserire    #info = models.ForeignKey('auth.User', on_delete=models.CASCADE)
      info = models.CharField(max_length=40)


def publish(self):
    self.published_date = timezone.now()
    self.save()
