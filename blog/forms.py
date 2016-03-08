from django import forms
from blog.models import blog_item

class UserForm(forms.Form): 
	email = forms.EmailField(label='Email', max_length=100)
	password = forms.CharField(widget=forms.PasswordInput, label='Password', max_length=100)

class LogoutForm(forms.Form):
	logout = forms.IntegerField(widget = forms.HiddenInput(),initial='1')

class BlogForm(forms.Form):
	title = forms.CharField(label = 'title' , max_length= 100 , initial = 'hello')
	#text = forms.TextField(label = 'content' , max_length=1000)
	text = forms.CharField(widget = forms.Textarea,label = 'content')

