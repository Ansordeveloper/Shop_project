from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=100) # Mavzu
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE) # foydalanuvchi 
    text = models.TextField() # Matn


    def __str__(self):
        return self.title
    
