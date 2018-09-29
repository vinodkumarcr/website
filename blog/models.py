from django.db import models

class blogs(models.Model):
    title=models.CharField(max_length=50)
    date=models.DateTimeField()
    image=models.ImageField(upload_to='images')
    summary=models.TextField(max_length=500)

    def __str__(self):
        return self.title
