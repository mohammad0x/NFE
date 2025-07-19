from  .views import *
from django.urls import path

app_name = 'APPNFE'


urlpatterns =[
     path('home/',home,name='home'),
     path('about/',about,name='about'),
     path('singlePost/<slug:slug>', singlePost, name='singlePost'),
     path('search/' , SearchResultsView.as_view() ,name='SearchResultsView'),
     path('product/', showProduc, name='showProduc'),
     path('like/<int:id>' , likeView , name='likeView'),
     path('mypage/',my_page, name='my_page'),
     path('chart/<slug:slug>', chart, name='chart'),
     path('contact/', contact_view, name='contact'),
     path('index/',index,name='index'),
     path('single/<slug:slug>',single,name='single'),


     
]


