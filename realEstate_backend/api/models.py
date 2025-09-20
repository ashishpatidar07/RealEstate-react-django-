from django.db import models

# Create your models here.

class Residency(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    detail = models.TextField()
    image = models.ImageField(upload_to="residencies/")

    def __str__(self):
        return self.name

class ContactMessage(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name