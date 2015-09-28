from django.shortcuts import render
from makemit.mailsignup.models import EmailForm, Email

def index(request):
  # if this is a POST request we need to process the form data
  if request.method == 'POST':
  	# create a form instance and populate it with data from the request:
  	form = EmailForm(request.POST)
   	# check whether it's valid:
   	if form.is_valid():
  		form.success = True
  		# print form.cleaned_data
  		email = Email(email=form.cleaned_data['email'])
  		# print email.email
  		email.save()

   	return render(request, 'index.jade', {'form': form})
  # if a GET (or any other method) we'll create a blank form
  else:
   	form = EmailForm()

  return render(request, 'index.jade', {'form': form})