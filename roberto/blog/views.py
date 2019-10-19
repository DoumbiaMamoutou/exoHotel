from django.shortcuts import render
from .models import *
from django.contrib.auth.models import User
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.


def index(request):
	arti = Article.objects.filter(status=True)
	tag = Tag.objects.all()
	paginator = Paginator(arti, 2)
	page = request.GET.get('page')
	prod = paginator.get_page(page)


	# try:
	# 	prod = paginator.get_page(page)
	# except PageNotAnInteger:
	# 	prod = paginator.page(1)
	# except EmptyPage:
	# 	prod = paginator.page(paginator.num_pages)

	email = request.POST.get('email')
	inst = Instagram.objects.all()
	
	
	if email is not None:
		h = Newsletter(email=email)
		h.save()

	data = {
		'prod': prod,
		'tag': tag,
		'inst': inst,
	}
	return render(request, 'blog/blog.html', data)

def single(request, id):
	email = request.POST.get('email')
	name = request.POST.get('name')
	emails = request.POST.get('email')
	web = request.POST.get('website')
	message = request.POST.get('message')


	arti = Article.objects.filter(status=True)  
	tag = Tag.objects.all()
	inst = Instagram.objects.all()
	com = Commentaire.objects.filter(status=True)
	so = Social.objects.all()
	
	if email is not None:
		h = Newsletter(email=email)
		h.save()

	if name is not None and emails is not None and web is not None and message is not None:
		me = Commentaire(nom=name,email=emails,website=web,message=message)
		me.save()

	print(email)
	ar = Article.objects.get(pk=id)
	data= {
		'ar': ar,
		'arti': arti,
		'tag': tag,
		'inst': inst,
		'com': com,
		'so': so,
	}
	return render(request, 'blog/single_blog.html', data)