from django.shortcuts import get_object_or_404, redirect, render

from blogs.models import Blog, Category
from django.contrib.auth.decorators import login_required

from dashboard.forms import CategoryForms


@login_required(login_url='login')
def dashboard(request):
    category_count = Category.objects.all().count()
    blogs_count = Blog.objects.all().count()

    data = {
        'category_count':category_count,
        'blogs_count':blogs_count
    }
    return render(request,'user/dashboard.html',data)


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





def blogs(request):
    return render(request,'dashboard/blogs.html')

