from django.forms import ModelForm
from .models import Post


class PostForm(ModelForm):

    class Meta:
        model = Post
        fields = ['author', 'title', 'post_type', 'category', 'text']


class PostUpdate(ModelForm):

    class Meta:
        model = Post
        fields = ['title', 'post_type', 'category', 'text']