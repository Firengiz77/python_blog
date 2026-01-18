from . import views
from django.urls import path

urlpatterns = [
    path('',views.dashboard, name='dashboard'),


    path('/categories/',views.categories,name="categories"),
    path('/categories/create',views.category_create,name="category.create"),
    path('/categories/store',views.category_store,name="category.store"),
    path('/categories/edit/<int:id>',views.category_edit,name="category.edit"),
    path('/categories/update/<int:id>',views.category_update,name="category.update"),
    path('/categories/delete/<int:id>',views.category_delete,name="category.delete"),



    path('/blogs/',views.blogs,name="blogs")
]