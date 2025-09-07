from django.shortcuts import get_object_or_404, redirect
from django.template.context_processors import request
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView
from django.urls import reverse_lazy
from django.contrib import messages
from .models import Post, Comment, Profile
from .forms import PostModelForm
from user_app.models import CustomUser

class ProfileListView(ListView):
    model = Post
    template_name = 'wall_app/wall.html'
    context_object_name = 'wall'

class UserPostListView(ListView):
    model = Post
    template_name = "wall_app/wall.html"
    context_object_name = "posts"

    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return reverse_lazy('wall_app:login')
        return super().get(self, request, *args, **kwargs)

    def get_queryset(self):
        return Post.objects.filter(wall_id=self.kwargs['pk'])

    # def get_queryset(self):
    #     author = get_object_or_404(AuthorProfile, author=self.kwargs.get('author'))
    #     if author:
    #         return Post.objects.filter(author=author.order_by("created_at"))
    #     messages.success(self.request, 'Пост успешно создан')

class ProfileDetailView(DetailView):
    model = Profile
    template_name = 'wall_app/profile_detail.html'
    context_object_name = 'profile_detail'


class PostDetailView(DetailView):
    model = Post
    template_name = 'wall_app/post_detail.html'
    context_object_name = 'post'

    def get(self, request, *args, **kwargs):
        post = self.get_object()
        post.views = getattr(post, 'views', 0) + 1
        post.save(update_fields=['views'])
        return super().get(request, *args, **kwargs)



class PostCreateView(CreateView):
    model = Post
    template_name = 'wall_app/post_create.html'
    form_class = PostModelForm
    # success_url = reverse_lazy('wall')

    def form_valid(self, form):
        form.instance.author_id = self.request.user.id # Profile.objects.get(pk=self.request.user.id).id
        form.instance.wall_id = self.kwargs['pk']

        res = super().form_valid(form)
        messages.success(self.request, 'Пост успешно создан')
        return res

    def get_success_url(self):
        return reverse_lazy('wall', kwargs={'pk': self.request.user.id})

class PostUpdateView(UpdateView):
    model = Post
    template_name = 'wall_app/edit_post.html'
    form_class = PostModelForm
    success_url = reverse_lazy('profile_detail')

    def form_valid(self, form):
        messages.success(self.request, 'Пост успешно обновлен')
        return super().form_valid(form)


class PostDeleteView(DeleteView):
    model = Post
    template_name = 'wall_app/delete_post.html'
    success_url = reverse_lazy('profile_detail')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Удаление продукта"
        context["description"] = "Вы уверены, что хотите удалить этот пост?"
        return context

    def form_valid(self, form):
        messages.success(self.request, "Пост успешно удален")
        return super().form_valid(form)




