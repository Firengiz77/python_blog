from django.shortcuts import render

from assignments.models import About
from blogs.models import Category, Blog


def home(request):
    categories = Category.objects.all()
    feature_post = Blog.objects.filter(is_feature=True,status=1).first()
    featured_posts = Blog.objects.filter(is_feature=True,status=1).exclude(id=feature_post.id)
    blogs = Blog.objects.filter(is_feature=False,status=1)

    try:
        about = About.objects.first()
    except:
        about = None

    data ={
        'categories':categories,
        'feature_post':feature_post,
        'featured_posts':featured_posts,
        'blogs':blogs,
        'about':about
        }
    return render(request,'home.html',data)