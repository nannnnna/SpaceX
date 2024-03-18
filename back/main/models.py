from django.db import models

class MainContent(models.Model):
    background_image = models.ImageField(upload_to='backgrounds/', blank=True, null=True)
    button_text = models.CharField(max_length=100)
    title_text = models.CharField(max_length=255)

class MenuItem(models.Model):
    name = models.CharField(max_length=50)
    url = models.CharField(max_length=100)
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.name
    
class Logo(models.Model):
    image = models.ImageField(upload_to='logos/')
    active = models.BooleanField(default=True) 

    def __str__(self):
        return f"{'Active' if self.active else 'Inactive'} Logo"

class Feature(models.Model):
    title = models.CharField(max_length=100)
    value = models.CharField(max_length=100)
    description = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.title