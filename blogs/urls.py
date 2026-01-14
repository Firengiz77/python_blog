from django.urls import include, path

from blogs import views

urlpatterns = [
    path('<int:category_id>/',views.blogs_by_category, name="blogs_by_category")
]