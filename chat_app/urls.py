from django.urls import path

from chat_app.views import UserListView, ChatView, MessageSendView

urlpatterns = [
    path("", UserListView.as_view(), name="chats"),
    path("<int:pk>", ChatView.as_view(), name="chat"),
    path("<int:pk>/send", MessageSendView.as_view(), name="chat-send"),
]
