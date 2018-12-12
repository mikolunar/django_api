from django import forms
from . models import Post


class PostForm(forms.Form):

    email = forms.EmailField(required=True)

    class Meta:
        model = Post
        fields = '__all__'
