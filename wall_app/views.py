from django.shortcuts import get_object_or_404
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
    context_object_name = "wall"

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
    success_url = reverse_lazy('wall')

    def form_valid(self, form):
        messages.success(self.request, 'Пост успешно создан')
        form.instance.author = self.request.user

        return super(PostCreateView, self).form_valid(form)

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




