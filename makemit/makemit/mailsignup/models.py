from django.db import models
from django import forms

class Email(models.Model):
  email = models.EmailField()

class EmailForm(forms.Form):
	email = forms.EmailField(label='Email')

	def clean_email(self):
		data = self.cleaned_data['email']
 		if Email.objects.all().filter(email=data).first() is not None:
			raise forms.ValidationError('Sorry, this email has already been registered.')

 		return data