from django.db import models

# Create your models here.
class contact (models.Model):
    name = models.CharField(max_length=120)
    email = models.CharField(max_length=150)
    phone = models.IntegerField()
    date  = models.DateField()
    desc = models.TextField()

    def __str__(self) :
        return self.name

    

    
