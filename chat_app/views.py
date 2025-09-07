from django.db.models import Q
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, DetailView, CreateView
from django.views.generic.base import TemplateResponseMixin

from chat_app.forms import MessageModelForm
from chat_app.models import Message
from user_app.models import CustomUser
from wall_app.models import Profile


class UserListView(ListView):
    model = CustomUser
    template_name = 'chat_app/user_list.html'
    context_object_name = 'profiles'

    def get_queryset(self):
        return Profile.objects.all()


class ChatView(View, TemplateResponseMixin):
    template_name = 'chat_app/chat.html'

    def get(self, request, *args, **kwargs):
        user_id = request.user.id
        id = self.kwargs['pk']

        recipient = CustomUser.objects.get(id=id)
        filter = (Q(sender_id=id) & Q(recipient_id=user_id)) | (Q(sender_id=user_id) & Q(recipient_id=id))
        chat_messages = Message.objects.filter(filter).order_by('created_at').all()

        return self.render_to_response({
            'recipient': recipient,
            'chat_messages': chat_messages
        })

class MessageSendView(CreateView):
    model = Message
    template_name = 'chat_app/chat.html'
    form_class = MessageModelForm

    def form_valid(self, form):
        form.instance.recipient_id = self.kwargs['pk']
        form.instance.sender_id = self.request.user.id
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('chat', kwargs={'pk': self.kwargs['pk']})
