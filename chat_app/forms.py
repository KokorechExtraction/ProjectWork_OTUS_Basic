from django import forms
from chat_app.models import Message


class MessageModelForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['body']
