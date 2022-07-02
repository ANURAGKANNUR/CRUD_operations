from django.db import models

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=250)
    age=models.IntegerField()
    active=models.BooleanField(default=True)

    def __str__(self):
        return self.name

