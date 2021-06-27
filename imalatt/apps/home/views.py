from django.shortcuts import render, redirect

def home_view(request):
    if request.user.is_authenticated:
        return redirect('home:kapilar')
    return render(request,'home.html')

def kapilar_view(request):
    return render(request,'kapilar.html')


def aboutsld_view(request):
    return render(request, "kapilar/aboutsld.html")



def view_401(request):

    return render(request,'401.html',{})