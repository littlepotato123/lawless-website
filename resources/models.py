from django.db import models

# Create your models here.
class Resources(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    link = models.CharField(max_length=300)

    def __str__(self):
        return self.title