from django import template
from blog.models import Post

register = template.Library()

@register.inclusion_tag('blog/popularposts.html')
def popularposts(arg=3):
    posts = Post.objects.filter(status=True).order_by('-counted_views')[:3]
    return {'posts':posts}