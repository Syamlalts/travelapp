from django.db import models

# Create your models here.

class place(models.Model):
    name=models.CharField(max_length=250)
    img=models.ImageField(upload_to='pics')
    des=models.TextField()

    def __str__(self):
        return self.name
class peoples(models.Model):
    names=models.CharField(max_length=350)
    imgs=models.ImageField(upload_to='photos')
    desc=models.TextField()

    def __str__(self):
        return self.names
