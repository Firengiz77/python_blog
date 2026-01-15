from django.shortcuts import get_object_or_404, redirect, render
from blogs.models import Blog, Category
from django.db.models import Q

def blogs_by_category(request,category_id):
    blogs = Blog.objects.filter(status=1,category=category_id)
    category = get_object_or_404(Category,pk=category_id) 
    # try:
    #      category = Category.objects.get(id=category_id)
    # except:
    #      return redirect('home')     
    data ={
        'blogs':blogs,
        'category':category
    }
    return render(request,'blogs.html',data)

def blogs(request, slug):
    # blog = Blog.objects.filter(slug=slug)
    blog = get_object_or_404(Blog, slug=slug, status=1)

    data = {
        'blog':blog
    }
    return render(request, 'blog.html',data)

def search(request):
    keyword = request.GET.get('keyword')
    blogs = Blog.objects.filter(Q(title__icontains=keyword) | Q(description__icontains=keyword),status=1)
    data ={
        'blogs':blogs,
        'keyword':keyword
    }
    return render(request,'search.html',data)