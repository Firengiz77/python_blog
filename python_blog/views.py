from django.shortcuts import render,redirect

from assignments.models import About
from blogs.models import Category, Blog
from python_blog.forms import RegistrationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import auth

def home(request):
    categories = Category.objects.all()
    feature_post = Blog.objects.filter(is_feature=True,status=1).first() or None
    featured_posts = Blog.objects.filter(is_feature=True,status=1).exclude(id=feature_post.id if feature_post else None)
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


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('register')
        else:
            form = RegistrationForm()
            print(form.errors)
    else:
        form = RegistrationForm()
        data={
            'form':form
        }
        return render(request,'user/register.html',data)
    

def login(request):
      if request.method == 'POST':
          form = AuthenticationForm(request, request.POST)
          if form.is_valid():
              username = form.cleaned_data['username']
              password = form.cleaned_data['password']

              user = auth.authenticate(username=username,password=password)
              if user is not None:
                  auth.login(request=request, user=user)
              return redirect('home')    
      
      else:    
        form = AuthenticationForm(request.POST)
        data ={
            'form':form
        }
        return render(request,'user/login.html',data)


def logout(request):
    auth.logout(request=request)
    return redirect('home')
