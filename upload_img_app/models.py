from django.db import models

class ModelFile(models.Model):
  image = models.ImageField(
    upload_to='documents/',
    verbose_name='画像1')
  image2 = models.ImageField(
    upload_to='documents2/',
    verbose_name='画像2')

