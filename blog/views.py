from django.shortcuts import render,get_object_or_404
from .models import blogs
def blog(request):
    blog=blogs.objects
    return render(request,'blog/home.html',{'site':blog})

def detail(request,blog_id):
    details=get_object_or_404(blogs,pk=blog_id)
    return render(request,'blog/detail.html',{'blog':details})
