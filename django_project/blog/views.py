from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from . import models
from django.views.generic import (CreateView,DeleteView,UpdateView,
                                    ListView,DetailView)

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
#JUST LIKE loginrequired




class post_list_view(ListView):
    model=models.Post
    template_name="blog/home.html" #app/model_viewtype.html
    context_object_name='posts'
    ordering=['-date_posted']
    paginate_by=2




class user_post_list_view(ListView):
    model=models.Post
    template_name="blog/user_post.html" #app/model_viewtype.html
    context_object_name='posts'
    ordering=['-date_posted']
    paginate_by=2

    def get_queryset(self):
        user=get_object_or_404(User,username=self.kwargs.get('username'))
        return models.Post.objects.filter(author=user).order_by("-date_posted")




class post_detail_view(DetailView):
    model=models.Post


class post_create_view(LoginRequiredMixin,CreateView):
    model=models.Post
    fields=['title','content']
    #looks for post_form.html in templates NOT post_create

    def form_valid(self, form):
        form.instance.author=self.request.user
        return super().form_valid(form)
        

class post_update_view(LoginRequiredMixin,CreateView):
    model=models.Post
    fields=['title','content']
    #looks for post_form.html in templates NOT post_create

    def form_valid(self, form):
        form.instance.author=self.request.user
        return super().form_valid(form)
        

def about(request): 
    #return HttpResponse("<h1>BLOG ABOUT</h1>")

    return render(request,"blog/about.html",{"title":" ABOUT ALAG"})










# posts=[
#         {
#             "author":"Akshay ",
#             "title":"My journey of ENGG",
#             "content":" Cricket-Football",
#             "date_posted":"December 20,2020"
#         },
#         {
#             "author":"James Bhai",
#             "title":"Atomic Habits",
#             "content":" Process>>GOAL",
#             "date_posted":"December 30,2020"
#         }
#     ]


# Create your views here.

# def home(request):
#     # return HttpResponse("<h1>BLOG HOME </h1>")
#     context={
#         "posts":Post.objects.all()
#     }
#     return render(request, "blog/home.html",context)

