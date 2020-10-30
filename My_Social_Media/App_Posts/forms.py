from django import forms
from App_Posts.models import Post_Model, Like_Model


class Post_Form(forms.ModelForm):
    class Meta:
        model = Post_Model
        fields = ('caption', 'post_pic')
