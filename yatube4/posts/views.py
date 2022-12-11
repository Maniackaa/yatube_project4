from django.shortcuts import get_object_or_404, render

from .models import Group, Post

NUMBERS_OF_POSTS = 10


def index(request):
    template = 'posts/index.html'
    posts = Post.objects.all()[:NUMBERS_OF_POSTS]
    context = {'posts': posts}
    return render(request, template, context)


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    # posts = Post.objects.filter(group=group).order_by('-pub_date')[:10]
    posts = group.group_posts.all()[:NUMBERS_OF_POSTS]
    template = 'posts/group_list.html'
    context = {
        'group': group,
        'posts': posts,
    }
    return render(request, template, context)
