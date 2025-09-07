from django import forms
from django.core.exceptions import ValidationError

from chat_app.models import Message


class MessageModelForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['body']
        labels = {
            'body': 'тельце',
        }
        widgets = {
            'body': forms.Textarea(attrs={'class': 'form-control', 'rows': 5, 'placeholder': 'Введите содержимое тельца'}),
        }


    def clean(self):
        cleaned_data = super().clean()
        content = cleaned_data.get('content')
        forbidden_words = ['пластмассовый мир победил']

        if content:
            for word in forbidden_words:
                if word in content.lower():
                    raise ValidationError(f'Пластмассовый мир идет нахуй вместе с тобой')