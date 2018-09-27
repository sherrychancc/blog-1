from django.shortcuts import render
from django.utils import timezone
from .models import Post

#. means this directory
#Take the actual blog posts from Posts (QuerySet) into the view

# Create your views here.

def post_list(request):
	posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	#Variable for our query set
	return render(request, 'blog/post_list.html', {'posts':posts})