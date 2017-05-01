
from django import forms
from . models import join
from django.contrib.auth import (
    authenticate, get_user_model, password_validation,
)

class JoinForm(forms.Form):
	email = forms.EmailField(widget=forms.TextInput({
		'class': 'form-control',
		'placeholder': '이메일'
		}))
	error_messages = {
    'password_mismatch': _("The two password fields didn't match."),
    }
	passwd1 = forms.CharField(widget=forms.PasswordInput({
		'class': 'form-control',
		'placeholder': '패스워드'
		}))
	passwd2 = forms.CharField(widget=forms.PasswordInput({
		'class': 'form-control',
		'placeholder': '패스워드확인'
		}))
	nick = forms.CharField(widget=forms.TextInput({
		'class': 'form-control',
		'placeholder': '닉네임'
		}))
	birth = forms.DateField(widget=forms.DateInput({
		'class': 'form-control',
		'placeholder': '생년월일'
		}))
'''
    def clean_password2(self):
        passwd1 = self.cleaned_data.get("passwd1")
        passwd2 = self.cleaned_data.get("passwd2")
        if passwd1 and passwd2 and passwd1 != passwd2:
            raise forms.ValidationError(
                self.error_messages['password_mismatch'],
                code='password_mismatch',
            )
        self.instance.email = self.cleaned_data.get('email')
        password_validation.validate_password(self.cleaned_data.get('passwd2'), self.instance)
        return passwd2
'''
    


	def save(self, commit=True):
		Join = join(**self.cleaned_data)
		if commit:
			Join.save()
		return Join
		'''