from django.shortcuts import render,redirect
from django.http import HttpResponse
from . import forms
from . import models

def issue(request):
    if(request.method=='POST'):
        market_form = forms.IssueForm(request.POST)
        username = request.session.get('user_name', None)
        bookname = request.POST.get('bookname')
        price = request.POST.get('price')
        major =request.POST.get('major')
        grade =request.POST.get('grade')
        qq =request.POST.get('qq')
        pic = request.POST.get('pic')
        type =request.POST.get('type')
        new_book = models.Market()
        new_book.username=username
        new_book.bookname=bookname
        new_book.price=price
        new_book.major=major
        new_book.grade=grade
        new_book.qq=qq
        new_book.pic=pic
        new_book.type=type
        new_book.save()
        return render(request,'market/issuedetail.html',locals())
    market_form=forms.IssueForm()
    return render(request,'market/issue.html',locals())

def list(request):
    booklist=models.Market.objects.all()
    context={'booklist':booklist}
    return render(request,'market/list.html',context)

def personal(request):
    username = request.session.get('user_name', None)
    booklist=models.Market.objects.filter(username=username)
    context={'booklist':booklist}
    return render(request,'market/personal.html',context)
def delete(request,id):
    username = request.session.get('user_name', None)
    now_book=models.Market.objects.get(id=id)
    if(username!=now_book.username):
        return HttpResponse('you have no permission to do this!')
    else:
        now_book.delete()
        return redirect('/personal/')
def search(request):
    if(request.method=='POST'):
        major = request.POST.get('major')
        grade = request.POST.get('grade')
        type = request.POST.get('type')
        booklist=models.Market.objects.filter(major=major,grade=grade,type=type)
        context = {'booklist': booklist}
        return render(request,'market/list.html',context)
    search_form=forms.SearchForm()
    return render(request,'market/search.html',locals())