from django.urls import path,include,re_path

from employee import views
urlpatterns = [
    path("home/",views.home_view,name="home"),
    path("login/",views.login_view,name="login"),
    path("logout/",views.logout_view,name="logout"),
    path("employees/",views.employees_details_view,name='employees'),
]