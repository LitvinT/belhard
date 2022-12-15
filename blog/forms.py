from django.forms import Form, EmailField, CharField, TextInput, EmailInput, Textarea, ModelForm
from .models import Contact


class ContactForm(ModelForm):
    name = CharField(
        widget=TextInput(
            attrs={
                'class': 'form-control',
                'id': 'name',
                'placeholder': 'Name'
            }
        ),
        max_length=64
    )
    email = EmailField(
        widget=EmailInput(
            attrs={
                'class': 'form-control',
                'id': 'email',
                'placeholder': 'Почта'
            }
        ),
        max_length=254
    )

    message = CharField(
        widget=Textarea(
            attrs={
                'class': 'form-control',
                'id': 'message',
                'style': 'height: 12rem',
                'placeholder': 'Message'
            }
        ),
        max_length=1024
    )


    class Meta:
        model = Contact
        fields = ('name', 'email', 'message')
