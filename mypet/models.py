from django.db import models

# Create your models here.
class Photo(models.Model):
    image = models.ImageField(blank=True, upload_to='media/') # 사진
    detail = models.CharField(max_length=200) # 사진 설명
    def __str__(self):
        return self.detail