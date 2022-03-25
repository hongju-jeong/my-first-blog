from django import forms   #json으로 serializer 하는거 비슷하게 form으로 형태만드는거
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'text',)