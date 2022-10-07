from django.db import models

# Create your models here.
class Finch(models.Model):
    name = models.CharField(max_length=100)
    img = models.CharField(max_length=250)
    info = models.CharField(max_length=500)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']

class Car(models.Model):
    make = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    chasis = models.CharField(max_length=50)
    finch = models.ForeignKey(Finch, on_delete=models.CASCADE, related_name='cars')

    def __str__(self):
        return self.make

class Body(models.Model):
    style = models.CharField(max_length=150)
    cars = models.ManyToManyField(Car)

    def __str__(self):
        return self.style
    
     
        
