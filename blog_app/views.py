from django.shortcuts import render,HttpResponse,get_object_or_404,redirect
from django.urls import reverse,reverse_lazy
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import *
from blog_app.forms import *
from blog_app.models import *

# Create your views here.

class post_list(ListView):
    model=posts

    def get_queryset(self):
        return posts.objects.order_by('-published_on')
    
class post_detail(DetailView):
    model=posts

class post_delete(DeleteView,LoginRequiredMixin):
    model=posts
    success_url=reverse_lazy("blog_app:post_list")

@login_required
def post_create(request,pk):
    post_user = get_object_or_404(User,pk=pk)

    if request.method == 'POST':
        form=post_form(request.POST,request.FILES)
        if form.is_valid():
            post_valid=form.save(commit=False)
            post_valid.user=post_user
            post_valid.save()
            return redirect('blog_app:post_list')
    form=post_form()
    return render(request, 'blog_app/posts_form.html',{'form':form})
    
def comment_create(request,pk):
    post_comment = get_object_or_404(posts,pk=pk)

    if request.method == 'POST':
        form=comment_form(request.POST)

        if form.is_valid():
            Comment=form.save(commit=False)
            Comment.user_comments=post_comment
            Comment.save()
            return redirect('blog_app:comment_detail',post_comment.pk)
        
    form=comment_form()
    return render(request, 'blog_app/comments_form.html',{'form':form})

def comment_detail(request,pk):
    comments=get_object_or_404(posts,pk=pk)
    return render(request, 'blog_app/comments_detail.html',{'post':comments})
