from django.shortcuts import render, get_object_or_404
from blog.models import Post, Category
import markdown
from comments.forms import CommentForm

# from django.http import HttpResponse

'''
def index(request):
    return render(request, 'blog/index.html', context={
        'title': '我的博客',
        'welcome': '我的博客首页'
    })
'''


# 主页
def index(request):
    post_list = Post.objects.all().order_by('-create_time')  # 正序, -create_time 逆序
    return render(request, 'blog/index.html', context={'post_list': post_list})


# 博客内容详情
def detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    # markdown
    post.body = markdown.markdown(post.body, extensions=['markdown.extensions.extra',
                                                         'markdown.extensions.codehilite',
                                                         'markdown.extensions.toc', ])
    comment_form = CommentForm()
    comment_list = post.comment_set.all()
    context = {
        'post': post,
        'comment_form': comment_form,
        'comment_list': comment_list,
    }
    return render(request, 'blog/detail.html', context=context)


# 归档页
def archives(request, year, month):
    post_list = Post.objects.filter(create_time__year=year,
                                    create_time__month=month
                                    ).order_by('-create_time')
    return render(request, 'blog/index.html', context={'post_list': post_list})


# 分类页
def category(request, pk):
    cate = get_object_or_404(Category, pk=pk)
    post_list = Post.objects.filter(category=cate).order_by('-create_time')
    return render(request, 'blog/index.html', context={'post_list': post_list})
