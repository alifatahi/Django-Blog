# Import Forms
from django import forms
# Import Model
from .models import Post


# Our Form Class
class PostForm(forms.ModelForm):
    # Our Class to declare model and fields
    class Meta:
        model = Post
        fields = [
            'title',
            'content'
        ]
