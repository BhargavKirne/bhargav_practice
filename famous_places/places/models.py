from django.db import models

class State(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Place(models.Model):
    name = models.CharField(max_length=200)
    state = models.ForeignKey(State, related_name='places', on_delete=models.CASCADE)
    description = models.TextField()

    def __str__(self):
        return self.name
