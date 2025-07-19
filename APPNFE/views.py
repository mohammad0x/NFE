from django.shortcuts import render , redirect,get_object_or_404

from .models import *
from django.views.generic import  ListView
from django.db.models import Q
from django.http import JsonResponse
from .forms import ContactForm
from django.contrib import messages



# Create your views here.


def home(request):
    post=Post.objects.filter(status="P").order_by("-publish")
    slider=Post.objects.filter(status="P", star=True).order_by("-publish")

    context={
        'post':post,
        'slider':slider
    }
    return render(request,'home.html',context)


def about(request) :
    return render(request,'about.html')


def singlePost(request,slug):
    single = get_object_or_404(Post , slug=slug)
    context = {
        'single':single,
    }
    return render (request , 'singlepost.html' , context)


class SearchResultsView(ListView):
    model = Post
    template_name = 'search.html'

    def get_queryset(self):
        query = self.request.GET.get("q")
        print(query)
        return Post.objects.filter(
            Q(title__icontains=query) | Q(des__icontains=query)
        )
        return object_list



def showProduc(request):
    post = Post.objects.all().order_by('-create')
    context = {
        'post': post,
    }
    return render(request, 'product.html', context)

    

def likeView(request , id ):
    url=request.META.get('HTTP_REFERER')
    if request.method == 'POST':
        post = id
        
        if Like.objects.filter( post_id = post ).exists():
            Like.objects.filter( post_id = post ).delete()
        else:
            Like.objects.create(post_id = post )
    return redirect(url)


def my_page(request):
    return render(request, 'singlepost.html')


def chart(request,slug):
    single = get_object_or_404(Post , slug=slug)
    context = {
        'single':single,
    }
    return render (request , 'chart.html' , context)




def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('APPNFE:contact')
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})



def index(request):
    post=Post.objects.filter(status="P").order_by("-publish")
    slider=Post.objects.filter(status="P", star=True).order_by("-publish")

    context={
        'post':post,
        'slider':slider
    }
    return render(request,'index.html',context)


def single(request,slug):
    single = get_object_or_404(Post , slug=slug)
    context = {
        'single':single,
    }
    return render(request,'single.html',context)