from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Post_Model(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_post')
    post_pic = models.ImageField(upload_to='post_pics', blank=True)
    caption = models.CharField(max_length=264, blank=True)
    upload_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-upload_date',]


class Like_Model(models.Model):
    post = models.ForeignKey(Post_Model, on_delete=models.CASCADE, related_name='post_like')
    liker = models.ForeignKey(User, on_delete=models.CASCADE, related_name='liker_like')

    def __str__(self):
        return '{} : {}'.format(self.liker, self.post)
