from django.db import models
from django.contrib.auth.models import User

class News(models.Model):
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    desciription = models.TextField()
    create_at = models.DateTimeField(auto_now_add=True)
    img = models.ImageField(upload_to='news-img/',null=True,blank=True)


    def __str__(self) -> str:
        return self.title




