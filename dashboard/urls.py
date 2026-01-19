from . import views
from django.urls import path

urlpatterns = [
    path('',views.dashboard, name='dashboard'),


# category crud
    path('/categories/',views.categories,name="categories"),
    path('/categories/create',views.category_create,name="category.create"),
    path('/categories/store',views.category_store,name="category.store"),
    path('/categories/edit/<int:id>',views.category_edit,name="category.edit"),
    path('/categories/update/<int:id>',views.category_update,name="category.update"),
    path('/categories/delete/<int:id>',views.category_delete,name="category.delete"),

# blog crud
    path('/blogs/',views.blogs,name="blogs"),
    path('/blogs/create',views.blogs_create,name="blogs.create"),
    path('/blogs/store',views.blogs_store,name="blogs.store"),
    path('/blogs/edit/<int:id>',views.blogs_edit,name="blogs.edit"),
    path('/blogs/update/<int:id>',views.blogs_update,name="blogs.update"),
    path('/blogs/delete/<int:id>',views.blogs_delete,name="blogs.delete"),
]