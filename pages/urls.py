from django.urls import path

from .views import HomePageView, Profile, AllPosts

from django.contrib.auth.decorators import login_required


urlpatterns =[
    path("",HomePageView.as_view(),name="home"),
    # path("profile",Profile,name="profile"),
    path("profile/",login_required(Profile.as_view()),name="profile"),
    path("allposts/",AllPosts.as_view(), name="allposts"),
]