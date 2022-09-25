from datetime import datetime
from django.db import models
import datetime

class Post(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to="blog/images")
    date = models.DateField(datetime.date.today)
    class Meta:
        verbose_name = "Registro"
        verbose_name_plural = "Registros"
    def __str__(self):
        return self.title

