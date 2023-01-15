from django.db import models

class BigBuisness(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
    
class SmallBusiness(models.Model):
    name = models.CharField(max_length=200)
    url = models.CharField(max_length=200)

    def __str__(self):
        return self.name + " " + self.url
