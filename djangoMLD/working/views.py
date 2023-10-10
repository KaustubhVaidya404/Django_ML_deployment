from django.shortcuts import render

def Welcome(request):
    return render(request, 'index.html')

def User(request):
    username = request.POST['username']
    print(username)
    return render(request, 'user.html', {'name':username})