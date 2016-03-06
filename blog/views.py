from django.shortcuts import render , redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
import urllib2
import urllib
import json
from django.views.decorators.csrf import csrf_exempt , csrf_protect , requires_csrf_token
from .forms import *
from django.contrib.sessions.backends.db import SessionStore

s = SessionStore()
def index(request):
	if 'cogni_id' not in s:
		if request.method == 'POST':
			form = UserForm(request.POST)
			if form.is_valid():
				a = str(form.cleaned_data['email']) 
				b = str(form.cleaned_data['password'])
				def extract_data(email , password):
					headers = { 'User-Agent' : 'Mozilla/5.0' }
					req = urllib2.Request('http://cognizance.org.in/cogni_api/login_app?session%5Bemail%5D='+ email + '&session%5Bpassword%5D=' + password , None, headers)
					html = urllib2.urlopen(req).read()
					d = json.loads(html)
					return(d)
				api_data = extract_data(a,b)

				def get_cogni_id(data):
					cog_id = data[u'cogni_id'][6:11]
					return(str(cog_id))

				def get_message(data):
					cog_message = data[u'message']
					return(cog_message)

				if (get_message(api_data)) == "Successfully logged in!" :
					s['cogni_id'] = get_cogni_id(api_data)
					s.save()
					return redirect('/blog/' + str(get_cogni_id(api_data) ))
				else:
					html = "<html><body> %s</body></html>" % str(get_message(api_data))
					return HttpResponse(html)
		else:
			form = UserForm()
			return render(request, 'blog/index.html', {'form': form})
	elif 'cogni_id' in s:
		return redirect('/blog/' + s['cogni_id'])

def user_page(request , pk):
	if 'cogni_id' in s:
		if request.method == 'POST':
			logout_form = LogoutForm(request.POST)
			blog_form = BlogForm(request.POST)
			a = logout_form.data['logout']
			a = int(a)
			if a == 1:
				del s['cogni_id']
				return redirect('/blog/')
			else:
				html = "<html><body> %s</body></html>" % request.session['cogni_id']
				return HttpResponse(html)

		else:
			cogni_id = 'COG16/' + str(pk)
			logout_form = LogoutForm()
			blog_form = BlogForm()
			#html = "<html><body> %s</body></html>" % s['cogni_id']
			#return HttpResponse(html)
			return render(request, 'blog/user_page.html' ,  {'logout_form': logout_form ,'blog_form':BlogForm , 'pk':pk , 'cogni_id':cogni_id})
	else:
		return redirect('/blog/' )

def save_blog(request):
	if request.method == 'POST':
		blog_form = BlogForm(request.POST)
		title= blog_form.data['title']
		text = blog_form.data['text']
		cogni_id = 'COG16/' + s['cogni_id']
		new_blog_item = blog_item(cog_id = cogni_id , title = title , text= text )
		new_blog_item.save()
		
		return redirect('/blog/' + s['cogni_id'])

	else:
		return redirect('/blog/')





    	


