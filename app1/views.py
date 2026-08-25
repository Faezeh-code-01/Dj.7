from django.shortcuts import render
dict={
    
    'Google':'http://google.com',
    'Apple':'http://apple.com',
    'Yahoo':'http://yahoo.com'
}

def index(request):
    return render (request, 'app1/index.html',{'links': dict})

def support_view(request):
    return render (request, 'app1/support.html' , {})