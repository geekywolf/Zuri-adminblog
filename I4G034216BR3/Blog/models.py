from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

User = get_user_model()
class Posts(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_date = models.DateField()
    published_date = models.DateField(auto_now_add=True)
