from django.db import models


class Car(models.Model):
    name=models.CharField(max_length=50)
    
    MODEL_CHOICES=[('FRD','Ford'), ('AUD','AUDI'), ('VW','Volkswagen')]
    model=models.CharField(max_length=3, choices=MODEL_CHOICES, default='1')

    CAR_TYPES=[('SEDAN', 'Sedan'), ('TURISMO','Turismo')]

    car_type=models.CharField(max_length=10, choices=CAR_TYPES, default='SEDAN')

    available=models.BooleanField()
    
    COLOR_CHOICES=[('RED', 'Red'), ('WHITE', 'White'), ('BLUE', 'Blue'),('BLACK', 'Black')]
    color=models.CharField(max_length=5, choices=COLOR_CHOICES, default='WHITE')

    registered_date=models.DateTimeField(auto_now_add=True)
    updated_date=models.DateTimeField(auto_now=True)

    location=models.URLField(blank=True)
    email=models.EmailField(blank=True)
    facebook=models.URLField(blank=True)
    #image=models.ImageField()
    description=models.TextField(blank=True)

    file = models.FileField(blank=True, null=True)
    remark = models.CharField(blank=True, max_length=20)
    #timestamp = models.DateTimeField(blank=True,  auto_now_add=True)
    
    def __str__(self):
        return self.name

class Rental (models.Model):

    name=models.CharField(max_length=50)
    rental_date=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Owner (models.Model):
    name=models.CharField(max_length=50)
    location=models.CharField(max_length=50)