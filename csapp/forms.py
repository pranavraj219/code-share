from django import forms
from django.contrib.auth.hashers import make_password
from csapp.models import Post
# from django_ace import AceWidget
class EditorForm(forms.ModelForm):
    class Meta():
        model = Post
        fields = ('title', 'src_lang', 'src_code', 'pwd')
        widgets = {
             'src_code' : forms.Textarea(attrs={'data-editor':'text', 'rows':15, 'cols':80}),
             'pwd' : forms.PasswordInput()
        }
    def clean_pwd(self):
        data = self.cleaned_data['pwd']
        print(data)
        data = make_password(data)
        return data
class AuthenticateForm(forms.ModelForm):
    class Meta():
        model = Post
        fields = ('pwd',)
        widgets = {
        'pwd' : forms.PasswordInput()
        }
