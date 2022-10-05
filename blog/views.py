from django.utils import timezone
from django.shortcuts import render, get_object_or_404, redirect
from blog.models import Post

def blog_view(request):
    # determining which post to show based on publish date
    now = timezone.now()
    posts = Post.objects.filter(published_date__lte=now)
    # setting status for published posts
    for post in posts:
        post.status = True
        post.save()

    context = {'posts':posts}
    return render(request, 'blog/blog.html', context)

def single_view(request, pid):
    try:
        post = Post.objects.get(id=pid, status=True)
        # counted view adding method
        post.counted_views += 1
        post.save()

        context = {'post':post}
        return render(request, 'blog/blog-single.html', context)    
    except:
        return redirect('/error')
