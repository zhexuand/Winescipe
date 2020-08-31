from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from homebase.models import ImagePost
from django.urls import reverse, reverse_lazy
from django.contrib.auth.forms import UserCreationForm



class HelloWorld(TemplateView):
    template_name = 'Hellotest.html'

class PostsView(ListView):
    model = ImagePost
    template_name = 'Index.html'
    
class PostDetailView(DetailView):
    model = ImagePost
    template_name = 'Image_detail.html'

class PostCreateView(CreateView):
    model = ImagePost
    template_name = 'ImagePost_create.html'
    fields = '__all__'
    
class PostUpdateView(UpdateView):
    model = ImagePost
    template_name = 'ImagePost_update.html'
    fields = '__all__'

class PostDeleteView(DeleteView):
    model = ImagePost
    template_name = 'ImagePost_delete.html'
    success_url = reverse_lazy("posts")
    
class SignUpView(CreateView):
    form_class = UserCreationForm
    template_name = 'Signup.html'
    success_url = reverse_lazy("login")
