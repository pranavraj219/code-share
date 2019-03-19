from django.urls import path, re_path
from csapp import views

urlpatterns = [
    path('', views.SubmitCode, name='submit_code'),
    re_path(r'^(?P<pk>\d+)/?', views.AuthenticateUser, name='post_authenticate'),
#    path('add_code/', views.DefaultView, name='add_code')
]
