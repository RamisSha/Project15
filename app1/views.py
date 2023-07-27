from django.shortcuts import render

# Create your views here.
def data (request):
    D={'Name':'Ramis Khan', 'Age':22}
    return render(request,'data.html',context=D)
