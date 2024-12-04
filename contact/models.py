from django.db import models

# Create your models here.
class Contact(models.Model):
   # attributes
   name = models.CharField(max_length=50)
   email = models.EmailField(max_length=100)
   phone = models.CharField(max_length=10)
   message = models.CharField(max_length=100)

   def __str__(self):
       return f"Message from {self.name}"

