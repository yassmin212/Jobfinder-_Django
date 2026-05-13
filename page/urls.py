from django.urls import path
from . import views
from application import views as app_views

urlpatterns = [
    path("", views.index, name="index"),
    path("login/", app_views.login_view, name="login"),
    path("signup/", app_views.signup_view, name="signup"),
    path("logout/", app_views.logout_view, name="logout"),
    path("search/", views.search_results, name="search_results"),
    path("admin-dashboard/", app_views.admin_dashboard, name="admin_dashboard"),
    path("admin-jobs/", views.admin_jobs, name="admin_jobs"),
    path("add-job/", views.add_job, name="add_job"),
    path("edit-job/", views.edit_job, name="edit_job"),
    path("applied-jobs/", app_views.applied_jobs, name="applied_jobs"),
    path("apply/<int:job_id>/", app_views.apply_for_job, name="apply_job"),
    path("jobs/", views.jobs, name="jobs"),
    path("job/<int:id>/", views.job_details, name="job_details"),
]
