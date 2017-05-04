from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserCreationForm(forms.ModelForm):
    """
    A form that creates a user, with no privileges, from the given username and
    password.
    """
    error_messages = {
        'password_mismatch': _("입력하신 두개의 암호가 일치하지 않습니다."),
    }
    password1 = forms.CharField(
        label=_("패스워드"),
        strip=False,
        widget=forms.PasswordInput,
    )
    password2 = forms.CharField(
        label=_("패스워드 확인"),
        widget=forms.PasswordInput,
        strip=False,
        help_text=_("이전 비밀번호와 동일하게 입력해 주세요"),
    )
    email = forms.EmailField(
        label=_("이메일"),
        widget=forms.TextInput,
        strip=False,
    )
    birth = forms.DateField(
        label=_("생년월일"),
        widget=forms.TextInput,
        strip=False,
    )

    class Meta:
        model = User
        fields = ("username", "password1", "password2", "email", "birth")
        field_classes = {'username': UsernameField}

    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)
        self.fields[self._meta.model.USERNAME_FIELD].widget.attrs.update({'autofocus': ''})
        self.fields['email'].widget.attrs['email'] = "email"
        self.fields['birth'].widget.attrs['birth'] = "birth"

    ##비번 유효성 검사##
    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(
                self.error_messages['password_mismatch'],
                code='password_mismatch',
            )
        self.instance.username = self.cleaned_data.get('username')
        password_validation.validate_password(self.cleaned_data.get('password2'), self.instance)
        return password2

    ##폼저장후 넘겨주기##
    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        user.email = self.cleaned_data['email']
        user.birth = self.cleaned_data['birth']
        
        if commit:
            user.save()
        return user