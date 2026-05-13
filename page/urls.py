from django.urls import path
from . import views

urlpatterns = [

    path('', views.index, name='index'),

    path('login/', views.login, name='login'),

    path('signup/', views.signup, name='signup'),

    path('search/', views.search_results, name='search_results'),

    path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),

    path('admin-jobs/', views.admin_jobs, name='admin_jobs'),

    path('add-job/', views.add_job, name='add_job'),

    path('edit-job/', views.edit_job, name='edit_job'),

    path('applied-jobs/', views.applied_jobs, name='applied_jobs'),

    path('jobs/', views.jobs, name='jobs'),

]