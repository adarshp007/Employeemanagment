from django.urls import path,include,re_path

from employee import views
urlpatterns = [
    path("",views.index,name="index"),
    path("login/",views.login_view,name="login"),
    path("logout/",views.logout_view,name="logout"),
    path("employees/",views.employee_view,name='employees'),
    path('users/', views.Employees.as_view(),name='users'),
    path('add_salary/',views.salary_view,name="salary"),
    path('register/',views.register_view,name='register'),
    path('user/details/<int:userid>',views.UserDetails.as_view(),name="userdetails"),
    path('user/update/<int:userid>',views.UserUpdate.as_view(),name="userupdate"),

    path('user/update/',views.user_update_view,name="userupdate"),  
    

]
