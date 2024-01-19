from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Blog(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    publication_date = models.DateField(auto_now_add=True)
    image = models.ImageField(upload_to='blog_images/')
    categories = models.ManyToManyField(Category)
    description = models.TextField()

    def __str__(self):
        return self.title

