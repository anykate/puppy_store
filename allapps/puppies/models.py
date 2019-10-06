from django.db import models


# Create your models here.
class Puppy(models.Model):
    """
    Puppy Model
    Defines the attributes of a puppy
    """
    name = models.CharField(max_length=255)
    age = models.PositiveSmallIntegerField(default=0)
    breed = models.CharField(max_length=255)
    color = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'puppies'

    def __str__(self):
        return self.name

    def get_breed(self):
        return f'{self.name} belongs to {self.breed} breed.'
