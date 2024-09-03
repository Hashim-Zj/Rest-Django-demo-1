from django.db import models

# Create your models here.


class BlogModel(models.Model):
  title=models.CharField(max_length=100)
  content=models.CharField(max_length=200)
  image=models.ImageField(upload_to='media')
  date=models.DateField(auto_now_add=True)

  