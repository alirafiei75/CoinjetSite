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

@register.inclusion_tag('blog/posttags.html')
def posttags():
    posts = Post.objects.filter(status=True)
    tags = set()
    for post in posts:
        for tag in post.tags.all():
            tags.add(tag.name)
    return {'tags':tags}
