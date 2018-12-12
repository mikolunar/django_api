from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Car(models.Model):
    name=models.CharField(max_length=50)
    
    MODEL_CHOICES=[(1,'Ford'), (2,'AUDI')]
    model=models.CharField(max_length=2, choices=MODEL_CHOICES, default=1)
    car_type=models.CharField(max_length=20)
    available=models.BooleanField()

    def __str__(self):
        return self.name
