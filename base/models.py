from django.db import models
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=200,null=False,blank=False)

    
    def __str__(self):
        return self.name

class Photo(models.Model):
    
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    title = models.CharField(max_length=100,null=True,blank=False)
    description = models.CharField(max_length=500,null=False,blank=False)
    image = models.ImageField(null=False,blank = False)

    def __str__(self):
        return self.description
