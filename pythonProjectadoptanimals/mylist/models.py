from django.db import models
# Create your models here.
class listsm(models.Model):
    animal_name=models.CharField(max_length=255)
    animal_description=models.TextField()
    animal_shortname=models.SlugField(max_length=255,unique=True)
    animal_published_date_time= models.DateTimeField(auto_now_add=True)
    animal_image=models.ImageField(upload_to='mylist/images',blank=True)
    def __str__(self):
          return self.animal_name