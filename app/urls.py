from _ast import pattern
from django.contrib import admin
from django.urls import path
from .import views

urlpatterns=[
    path('admin/', admin.site.urls),
    path("",views.home,name='home'),
    path("home",views.home,name='home'),
    path('loginn',views.loginn),
    path('signup',views.register),
    path('post',views.postadd),
    path('contact',views.contact),
    path('cat',views.category),
    path('about',views.about),
    path('offermessages', views.offers),
    path('send-interest/<int:pk>', views.addinterest, name='send-interest'),
    path('service',views.service),
    path('blog',views.blog),
    path('blog-left-sidebar',views.blogleft),
    path('bloggridfull',views.blogfull),
    path('singlepost',views.blogsingle),
    path('adgrid',views.adgrid),
    path('adlist',views.adlist),
    path('ads-details',views.addetail),
    path('pricing',views.package),
    path('testimonial',views.testimonial),
    path('faq',views.faq),
    path('404',views.error),
    path('payments',views.payments),
    path('dashboard',views.dashboard),
    path('logout',views.logout),
    path('view/<int:pk>',views.prodetail,name='view'),
    path('searchgo',views.item_search),
    #database link
    path('register',views.signup),
    path('signin',views.signin),
    path('submit',views.adds),
    path('admindashboard',views.admin),
    path('usser',views.usser),
    ]