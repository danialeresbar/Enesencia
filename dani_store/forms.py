from django import forms
from users.models import User


class RegisterForm(forms.Form):
    username = forms.CharField(
        label="Usuario",
        required=True,
        min_length=5,
        max_length=10,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "id": "username",
                "placeholder": "username"
            }
        )
    )
    email = forms.EmailField(
        label="Correo electrónico",
        required=True,
        widget=forms.EmailInput(
            attrs={
                "class": "form-control",
                "id": "email",
                "placeholder": "example@mail.com"
            }
        )
    )
    password = forms.CharField(
        label="Contraseña",
        required=True,
        min_length=5,
        max_length=10,
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "id": "password"
            }
        )
    )
    password_confirm = forms.CharField(
        label="Confirma tu contraseña",
        required=True,
        min_length=5,
        max_length=10,
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "id": "password_confirm"
            }
        )
    )

    def clean(self):
        cleaned_data = super().clean()
        key = cleaned_data.get("password")
        if not key == cleaned_data.get("password_confirm"):
            self.add_error("password_confirm", "Las contraseñas no coinciden")

    def save_user(self):
        return User.objects.create_user(
            self.cleaned_data.get("username"),
            self.cleaned_data.get("email"),
            self.cleaned_data.get("password")
        )
