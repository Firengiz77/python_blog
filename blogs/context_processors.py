from assignments.models import SocialMedia
from blogs.models import Category

def get_categories(request):
    categories = Category.objects.all()
    return dict(categories=categories)


def get_social_media(request):
    social_media = SocialMedia.objects.all()
    return dict(social_media=social_media)
