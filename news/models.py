from django.db import models

# Create your models here.
from django.db import models

class News(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    content = models.TextField()
    author = models.CharField(max_length=100, null=True, blank=True)
    published_at = models.DateTimeField()
    source = models.CharField(max_length=100)
    url = models.URLField()
    image_url = models.URLField(null=True, blank=True)
    category = models.CharField(max_length=100)

    def __str__(self):
        return self.title
    
class Visitor(models.Model):
    name = models.CharField(max_length=100)
    visited_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name