from django import forms
from blogs.models import Blog, Category


class CategoryForms(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'

class BlogForms(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ('title','description','category','image','status','is_feature',)