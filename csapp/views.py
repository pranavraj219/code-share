from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView, FormView, CreateView, DetailView
from django.urls import reverse_lazy
from csapp.forms import EditorForm, AuthenticateForm
from csapp.models import Post
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password, check_password
import sys


# Create your views here.
# class DefaultView(CreateView):
#     form_class = EditorForm
#     model = Post

def DetailViewFun(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'csapp/code.html', context={'post':post, 'isReadOnly':'false'})

def AuthenticateUser(request, pk):
    try:
        post = get_object_or_404(Post, pk=pk)
    except Post.DoesNotExist:
        raise Http404("Page Does Not Exist!! :P")
    if request.method == 'POST':
        form = AuthenticateForm(request.POST)
        if form.is_valid():
            if check_password(form.cleaned_data['pwd'], post.pwd):
                print('user authenticated ' + post.title + ' ' + str(post.pk), file = sys.stderr)
                return DetailViewFun(request, pk)
            else:
                print('user failed ' + post.title + ' ' + str(post.pk), file = sys.stderr)
                return HttpResponse("Passwords do not match!")
    else:
        form = AuthenticateForm()
    return render(request, 'csapp/post_authenticate.html', {'form':form, 'post':post})


def SubmitCode(request):
    if request.method == 'POST':
        form = EditorForm(request.POST)
        if form.is_valid():
            new_code = form.save()
            print('code submitted ' + new_code.title + ' ' + str(new_code.pk), file = sys.stderr)
            return redirect('post_authenticate', pk = new_code.pk)
        else:
            return HttpResponse("Page Not Found!!")


    else:
        form = EditorForm()
    return render(request, 'csapp/post_form.html', {'form':form, 'isReadOnly':'false'})
    #return HttpResponse("Page Not Found!!")
