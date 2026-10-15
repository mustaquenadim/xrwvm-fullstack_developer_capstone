from django.db import models
from django.utils.timezone import now
from django.core.validators import MaxValueValidator, MinValueValidator


# Car Make model
class CarMake(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    country = models.CharField(max_length=100, blank=True)
    founded_year = models.IntegerField(null=True, blank=True)
    created_at = models.DateTimeField(default=now)

    def __str__(self):
        return self.name  # Return the name as the string representation


# Car Model model
class CarModel(models.Model):
    # Many-to-One relationship: one Car Make has many Car Models
    car_make = models.ForeignKey(CarMake, on_delete=models.CASCADE)
    # Refers to a dealer created in the Cloudant/Mongo database
    dealer_id = models.IntegerField(default=1)
    name = models.CharField(max_length=100)
    CAR_TYPES = [
        ('SEDAN', 'Sedan'),
        ('SUV', 'SUV'),
        ('WAGON', 'Wagon'),
        ('COUPE', 'Coupe'),
        ('HATCHBACK', 'Hatchback'),
    ]
    type = models.CharField(max_length=10, choices=CAR_TYPES, default='SUV')
    year = models.IntegerField(default=2023,
                               validators=[
                                   MaxValueValidator(2023),
                                   MinValueValidator(2015)
                               ])
    color = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.car_make.name + " " + self.name
