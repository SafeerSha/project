from django.contrib import messages
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from .models import shop, userimage, interests
from.filter import itemFilter
# PAGE BUTTONS

def home(request):
    if 'id' in request.session:
        return redirect(usser)
    else:
        data = shop.objects.all()[:6]
        return render(request, "index.html",{"items":data})
def loginn(r):
    return render(r, 'login.html')
def register(r):
    return render(r, 'register.html')
@login_required(login_url=loginn)
def postadd(r):
    return render(r, 'post-ads.html')
def contact(r):
    return render(r, 'contact.html')
def category(r):
    return render(r, 'category.html')
def about(r):
    return render(r, 'about.html'),
def service(r):
    return render(r, 'services.html'),
def blog(r):
    return render(r,'blog.html'),
def blogleft(r):
    return render(r,'blog-left-sidebar.html')
def blogfull(r):
    return render(r,'blog-grid-full-width.html')
def blogsingle(r):
    return render(r,'single-post.html')
def adgrid(r):
    return render(r,'adlistinggrid.html')
def adlist(r):
    return render(r,'adlistinglist.html')
def addetail(r):
    return render(r,'ads-details.html')
def package(r):
    return render(r,'pricing.html')
def testimonial(r):
    return render(r,'testimonial.html')
def faq(r):
    return render(r,'faq.html')
def error(r):
    return render(r,'404.html')
def payments(r):
    return render(r,'payments.html')
def dashboard(r):
    return render(r,'dashboard.html')
def logout(r):
    logout(r)
    return render(r,'login.html')
def postad(r):
    if r.method == 'POST':
        return render(r,'post-ads.html')
    else:
        return redirect(r,"login.html")
def prodetail(r,pk):
    detail = shop.objects.get(pk=pk)
    return render(r,'ads-details.html',{"d":detail})


#database link
def signup(request):
    if request.method == 'POST':
        username = request.POST['user']
        first_name = request.POST['fname']
        email = request.POST['e1']
        password = request.POST['p1']
        retypepassword = request.POST['rp1']
        profpic = request.FILES.get('propic')
        myuser = User.objects.create_user(username, email, password)
        myuser.first_name = first_name
        myuser.save()
        image = userimage(user=myuser, image=profpic)
        image.save()
        messages.success(request,'Succesfully Registered')
        return render(request, 'login.html')


def signin(request):
    if request.method == 'POST':
        user1 = request.POST['user']
        pass1 = request.POST['p1']
        user = authenticate(username=user1, password=pass1)
        if user is not None:
            if user.is_staff == True:
                login(request, user)
                return redirect(admin)
            else:
                request.session['id'] = user.username
                login(request, user)
                return redirect(usser)
        else:
            return HttpResponse("INVALID USER")
def admin(r):
    return render(r,"admindashboard.html")
def usser(r):
    sr = shop.objects.all()[:6]
    return render(r,"userindex.html", {'items': sr})

def adds(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            a = request.POST['product']
            i = request.POST['category']
            b = request.POST['price']
            c = request.FILES['file']
            d = request.POST['Name']
            e = request.POST['phone']
            f= request.POST['address']
            g = request.POST['country']
            h = request.POST['state']
            j = request.POST['about']
            user = User.objects.get(id=request.user.id)
            un = user.username
            z = shop(user=un, product=a,price=b,file=c,Name=d,phone=e,address=f,country=g,state=h,category=i,about=j)
            z.save()
            return render(request,'post-ads.html')

@login_required(login_url=signin)
def addinterest(request, pk):
    if request.user.is_authenticated:
        if request.method == 'POST':
            a = request.POST['email']
            b = request.POST['phone']
            user = User.objects.get(id=request.user.id)
            un = user.username
            z = shop.objects.get(pk=pk)
            uname = z.user
            title = z.product
            x = interests(senduser=un,aduser=uname,product=title,phone=b,email=a)
            x.save()
            return redirect(usser)



def offers(request):
    if request.user.is_authenticated:
        user = User.objects.get(id=request.user.id)
        un = user.username
        data = interests.objects.filter(aduser=un)
        return render(request, 'offermessages.html', {'data': data})

# search item
def nodata(r):
    return render(r,'nodisplay.html')

def item_search(request):
    context = {}
    filtered_items = itemFilter(
        request.GET,queryset=shop.objects.all()
    )
    context['filtered_items'] = filtered_items
    return render(request,'searchdisplay.html',context=context)


