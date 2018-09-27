from django import forms
from .models import Post

class PostForm(forms.ModelForm):
	class Meta: #which model to use to create the form
		model = Post
		fields = ('title', 'text') 