from django import forms
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
class login_form(forms.Form):
	username = forms.CharField(required = True)
	password = forms.CharField(required = True)


class register_form(forms.ModelForm):
	Confirm_password = forms.CharField(required = True)
	email = forms.EmailField(required=True)
	class Meta:
		model = User
		fields = ['username', 'email','password','Confirm_password']

	def clean(self):
		cleaned_data = super(register_form,self).clean()
		password = cleaned_data.get("password")
		password2 = cleaned_data.get('Confirm_password')
		email = cleaned_data.get("email")

		if (password and password2 and password2 == password) :
			return cleaned_data
		else :
			raise forms.ValidationError(_("Both password does not match."))
