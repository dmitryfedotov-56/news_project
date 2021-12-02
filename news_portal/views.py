from django.shortcuts import render
from django.views import View
# Create your views here.

from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from .models import Post, Category
from django.views import View
from django.core.paginator import Paginator
from .filters import PostFilter
from .forms import PostForm, PostUpdate

# Create your views here.

'''
class PostList(ListView):
    model = Post
    template_name = 'post.html'
    context_object_name = 'posts'
    queryset = Post.objects.order_by('-id')
'''

'''
class PostList(View):
    def get(self, request):
        posts = Post.objects.order_by('-id')
        p = Paginator(posts, 1)
        posts = p.get_page(request.GET.get('page',1))
        data = {'posts':posts}
        return render(request,'post.html',data)
'''


class PostList(ListView):
    model = Post
    template_name = 'post.html'
    context_object_name = 'posts'
    ordering = ['-id']
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = PostFilter(self.request.GET, queryset=self.get_queryset())

        context['categories'] = Category.objects.all()
        context['form'] = PostForm()
        return context

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            form.save()

        return super().get(request, *args, **kwargs)


class PostDetail(DetailView):
    model = Post
    template_name = 'post_detail.html'
    context_object_name = 'post_detail'


class PostCreate(CreateView):
    template_name = 'create_post.html'
    form_class = PostForm


class PostDelete(DeleteView):
    template_name = 'delete_post.html'
    context_object_name = 'post_detail'
    queryset = Post.objects.all()
    success_url = '/news/'


class PostUpdate(UpdateView):
    template_name = 'update_post.html'
    form_class = PostUpdate

    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return Post.objects.get(pk = id)
