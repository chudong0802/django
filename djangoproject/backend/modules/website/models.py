from django.db import models
from django.utils import timezone

class Blog(models.Model):
    title = models.CharField(max_length=50)
    content = models.CharField(max_length=100)
    class Meta:
        db_table = 't_website'

class Project(models.Model):
    name = models.CharField(max_length=50)
    create_time = models.DateTimeField(default=timezone.now)
    update_time = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name




    # Create your models here.
