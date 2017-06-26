from django.conf.urls import url
from .  import views
from .views import Home, Home_main

urlpatterns = [
#            url(r'^$',views.home , name="home"),
            url(r'^$',Home.as_view(),name="home"),
            url(r'^home/$',Home_main.as_view(), name="home_main"),
]
