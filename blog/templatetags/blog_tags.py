from django import template
from blog.models import Post, Category

register = template.Library()

@register.inclusion_tag('blog/popularposts.html')
def popularposts(arg=3):
    posts = Post.objects.filter(status=True).order_by('-counted_views')[:arg]
    return {'posts':posts}

@register.inclusion_tag('blog/postcategories.html')
def postcategories():
    posts = Post.objects.filter(status=1)
    categories = Category.objects.all()
    cat = {}
    for name in categories:
        cat[name] = posts.filter(category=name).count()
    return {'categories':cat}
