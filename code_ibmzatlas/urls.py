from django.contrib import admin
from django.urls import path
from posts import views as post_views
from references import views as ref_views
from users import views as users_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', post_views.list_post),
    path('references/', ref_views.references_db),
    path('login/',users_views.login),
    path('register/',users_views.register),
    path('user/home',users_views.home),
    path('user/home',users_views.profile),
]
