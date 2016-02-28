from django.shortcuts import render
from django.core.paginator import Paginator
from  blog.models import *
from django.http import HttpResponse
import datetime,time
def index(request):
     try:
    	 page_num = int(request.GET.get('page'))
     except:
     	 page_num = 1
     posts = Blog.objects.all()
     p= Paginator(posts,7)
     page = p.page(page_num)
     category = Category.objects.all()
     return render(request,'index.html',{'posts':page, 'category':category})
	
def show(request,id):
	post = Blog.objects.get(id = id)
	category = Category.objects.all()
	return render(request,'show.html',{'post':post,'category':category})

def list(request,id):
	category = Category.objects.all()

	list  = Blog.objects.filter(category__id__exact = id )
	name = list[0].category
	try:
		page_num = int (request.GET.get('page'))
	except:
		page_num = 1
	p= Paginator(list,7)
	page = p.page(page_num)
	return render(request,'list.html',{'lists':page,'category':category,'name':name})
def uedit(request,id):
	if request.user.is_authenticated():
		category = Category.objects.all()
		try:
			post = Blog.objects.get(id = id)
		except:
			post = 0

		return render(request,'uedit.html',{'category':category,'post':post})
	else:
		return HttpResponse("没有权限访问")
def send(request):
	title = request.POST.get('title')
	category = request.POST.get('category')
	print(category)
	content= request.POST.get("content")
	try : 
		
		post = Blog.objects.get(title = title )
		post.title = title 
		post.category = Category.objects.all()[int(category) - 1]
		post.content = content
		publish_time = datetime.datetime.now()
		post.save()
		return HttpResponse("修改文章成功！")
	except:
		Blog.objects.create(title = title ,category = Category.objects.all()[int(category) - 1],content =content,publish_time = datetime.datetime.now())
		#return render(request,'concent.html',{"concent":concent,'title':title,'category':category})
		return HttpResponse("新建文章成功！！")
