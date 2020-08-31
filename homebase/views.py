from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from homebase.models import ImagePost, Like
from django.urls import reverse, reverse_lazy
from homebase.forms import CustomUserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from annoying.decorators import ajax_request



class HelloWorld(TemplateView):
    template_name = 'Hellotest.html'

class PostsView(ListView):
    model = ImagePost
    template_name = 'Index.html'
    
class PostDetailView(DetailView):
    model = ImagePost
    template_name = 'Image_detail.html'

class PostCreateView(LoginRequiredMixin, CreateView):
    model = ImagePost
    template_name = 'ImagePost_create.html'
    fields = '__all__'
    login_url = 'login'
    
class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = ImagePost
    template_name = 'ImagePost_update.html'
    fields = '__all__'
    login_url = 'login'

class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = ImagePost
    template_name = 'ImagePost_delete.html'
    success_url = reverse_lazy("posts")
    login_url = 'login'
    
class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'Signup.html'
    success_url = reverse_lazy("login")
    
@ajax_request
def addLike(request):
    post_pk = request.POST.get('post_pk')
    post = ImagePost.objects.get(pk=post_pk)
    try:
        like = Like(post=post, user=request.user)
        like.save()
        result = 1
    except Exception as e:
        like = Like.objects.get(post=post, user=request.user)
        like.delete()
        result = 0

    return {
        'result': result,
        'post_pk': post_pk
    }
