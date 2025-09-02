from django.db import models

class Angilal (models.Model):
    aname = models.CharField(max_length=200)
    def __str__(self):
        return self.aname
    
class Baraa (models.Model):
    bname = models.CharField(max_length=200)
    angilal = models.ForeignKey(Angilal,on_delete=models.CASCADE)
    price = models.PositiveBigIntegerField(default=0)
    def __str__(self):
        return f"{self.bname}({self.angilal})({self.price})"