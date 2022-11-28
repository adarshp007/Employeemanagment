from django.urls import path,include

from employee import views
urlpatterns = [
    
    path("login/",views.login,name="login")
]