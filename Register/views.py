from unicodedata import name
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from .models import Post,Registration,Users
from django.urls import reverse

name = ''
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        users = Users.objects.all().values()
        for user in users:
            if user["userlist"] == username:
                global name
                print(username)
                name = username
                if user['passlist'] == password:
                    return HttpResponseRedirect(reverse('home'))

    else:
        print("login failed.")
    template = loader.get_template("login.html")
    return(HttpResponse(template.render({}, request)))

def logdata(request):
    return HttpResponseRedirect(reverse('home'))


def register(request):
    template = loader.get_template("register.html")
    return(HttpResponse(template.render({}, request)))

def home(request):
    desc = Registration.objects.all().values()
    n=0
    for i in desc:
        if i['user_name'] == name:
            print(i)
            break
        n+=1    
    about = desc[n]["about"]
    uname = desc[n]["user_name"]
    
    posts = Post.objects.all().values()
    print(posts)
    data=[]
    for i in posts:
        
        if i['author'] == name:
           data.append(i)
           
    data = list(data)
    
    data.reverse()
    template = loader.get_template('homepage.html')
    context = {
        'data' : data,
        'log_name' : uname,
        'about':about
    }
    return(HttpResponse(template.render(context, request)))

def newpost(request):
    template = loader.get_template("newpost.html")
    return(HttpResponse(template.render({}, request)))

def delete(request, id):
    post = Post.objects.get(id=id)
    print(post)
    post.delete()
    return(HttpResponseRedirect(reverse('home')))

def newpostadd(request):
    d1 = request.POST['title']
    d2 = request.POST['category']
    d3 = request.POST['pdata']
    d4 =  name
    post = Post(title=d1, category=d2, pdata=d3, author = d4)
    print(name)
    post.save()
    return HttpResponseRedirect(reverse('home'))

def newuser(request):
    
    
    d1=request.POST['username']
    d2=request.POST['password']
    d3=request.POST['email']
    d4=request.POST['dob']
    d5=request.POST['about']
    user=Registration(user_name=d1,password=d2,email=d3,dob=d4,about=d5)
    user.save()
    log=Users(userlist=d1,passlist=d2)
    log.save()
    print(Registration.objects.all())
    return HttpResponseRedirect(reverse('login'))


def profile(request):
    template = loader.get_template("profile.html")
    desc = Registration.objects.all().values()
    n=0
    for i in desc:
        if i['user_name'] == name:
            
            break
        n+=1
    
    
    about = desc[n]["about"]
    uname = desc[n]["user_name"]
    dob = desc[n]["dob"]
    email = desc[n]["email"]
    context = {"log_name":uname,
                "about":about,
                "dob":dob,
                "email":email,              
                }
    
    return(HttpResponse(template.render(context)))


def edit(request, id):
    post = Post.objects.get(id=id)
    template=loader.get_template("edit.html")
    context={
        'post':post,
    }
    return(HttpResponse(template.render(context,request)))

def editpost(request,id):
    d1 = request.POST['title']
    d2 = request.POST['category']
    d3 = request.POST['pdata']
    
    post=Post.objects.get(id=id)
    post.title=d1
    post.category=d2
    post.pdata=d3
    post.save()
    return HttpResponseRedirect(reverse('home'))

# Create your views here.
