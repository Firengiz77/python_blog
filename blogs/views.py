from django.shortcuts import get_object_or_404, redirect, render
from blogs.models import Blog, Category


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


