from django import forms
from django.core.exceptions import ValidationError

from wall_app.models import Post


class PostModelForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['content', 'tags']
        labels = {
            'content': 'Содержание',
            'tags': 'Тэги'
        }
        widgets = {
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 5, 'placeholder': 'Введите содержимое поста'}),
            'tags': forms.SelectMultiple(attrs={'class': 'form-control'}),
        }


    def clean(self):
        cleaned_data = super().clean()
        content = cleaned_data.get('content')
        forbidden_words = ['пластмассовый мир победил']

        if content:
            for word in forbidden_words:
                if word in content.lower():
                    raise ValidationError(f'Пластмассовый мир идет нахуй вместе с тобой')