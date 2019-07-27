from django.shortcuts import render
from post.models import Post

# Create your views here.

def post_list(request):
    posts = Post.objects.all()
    return render(request, 'post/post_list.html', {'posts': posts})