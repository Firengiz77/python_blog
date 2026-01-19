from django.shortcuts import get_object_or_404, redirect, render

from blogs.models import Blog, Category
from django.contrib.auth.decorators import login_required

from dashboard.forms import BlogForms, CategoryForms
from django.template.defaultfilters import slugify

@login_required(login_url='login')
def dashboard(request):
    category_count = Category.objects.all().count()
    blogs_count = Blog.objects.all().count()

    data = {
        'category_count':category_count,
        'blogs_count':blogs_count
    }
    return render(request,'user/dashboard.html',data)



# Category crud
def categories(request):
    categories = Category.objects.filter()

    data = {
        'categories':categories
    }

    return render(request,'dashboard/category/index.html',data)


def category_create(request):
     form = CategoryForms()
     data = {
            'form':form
        } 
     return render(request,'dashboard/category/create.html',data)


def category_store(request):
    form = CategoryForms(request.POST)
    if form.is_valid:
        form.save()
        return redirect('categories')
    else:
     return redirect('categories')


def category_edit(request,id):
     category = get_object_or_404(Category,pk=id) 
     form = CategoryForms(instance=category)
     data = {
            'form':form,
            'category':category
        } 
     return render(request,'dashboard/category/edit.html',data)


def category_update(request,id):
    category = get_object_or_404(Category,pk=id) 
    form = CategoryForms(request.POST,instance=category)
    if form.is_valid:
        form.save()
        return redirect('categories')
    else:
     return redirect('categories')

def category_delete(request,id):
     category = get_object_or_404(Category,pk=id) 
     category.delete()
     return redirect('categories')




# Blogs crud

def blogs(request):
    blogs = Blog.objects.all()
    data ={
        'blogs':blogs
    }
    return render(request,'dashboard/blogs/index.html',data)

def blogs_create(request):
     form = BlogForms()
     data = {
            'form':form
        } 
     return render(request,'dashboard/blogs/create.html',data)

def blogs_store(request):
    form = BlogForms(request.POST,request.FILES)
    if form.is_valid:
        blog = form.save(commit=False)
        blog.author = request.user
        blog.save()
        blog.slug = slugify(form.cleaned_data['title'])
        blog.save()
        return redirect('blogs')
    else:
     print('Is not valid')
     return redirect('blogs')

def blogs_edit(request,id):
     blog = get_object_or_404(Blog,pk=id) 
     form = BlogForms(instance=blog)
     data = {
            'form':form,
            'blog':blog
        } 
     return render(request,'dashboard/blogs/edit.html',data)

def blogs_update(request,id):
    blogs = get_object_or_404(Blog,pk=id) 
    form = BlogForms(request.POST,request.FILES,instance=blogs,)
    if form.is_valid:
        blog = form.save()
        blog.slug = slugify(form.cleaned_data['title'])
        blog.save()
        return redirect('blogs')
    else:
     return redirect('blogs')

def blogs_delete(request,id):
     blog = get_object_or_404(Blog,pk=id) 
     blog.delete()
     return redirect('blogs')

