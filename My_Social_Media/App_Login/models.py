from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class User_Profile_Model(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="up_model_user")
    full_name = models.CharField(max_length=264, blank=True)
    contact = models.CharField(max_length=14, blank=True)
    dob = models.DateField(blank=True, null=True)
    website = models.URLField(blank=True)
    fb_acc = models.URLField(blank=True)
    pro_pic = models.ImageField(blank=True, upload_to='profile_pics')

    def __str__(self):
        return self.user.username


class Follow_Model(models.Model):
    follower = models.ForeignKey(User, on_delete=models.CASCADE, related_name='follower_follow')
    following = models.ForeignKey(User, on_delete=models.CASCADE, related_name='following_follow')
    follow_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '"{}" follows "{}"'.format(self.follower, self.following)
