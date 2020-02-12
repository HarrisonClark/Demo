from django.db import models

# Create your models here.
class Submission(models.Model):
    name = models.CharField(max_length=30)
    date = models.DateTimeField()
    link = models.URLField()

    def __str__(self):
        return self.name + ": " + self.link
