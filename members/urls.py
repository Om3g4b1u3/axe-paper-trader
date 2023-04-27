#> 'members' URL Configuration <#
from django.urls import path
from . import views

urlpatterns = [
	path('', views.main, name='main'),
	path('members/', views.members, name='members'),
	path('members/member_details/<int:id>', views.member_details , name='member_details'),
	path('testing/', views.testing, name='testing'),
]
