
from django.contrib import admin
from django.urls import path,include
from .import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('Api/v1/', include('ApiApp.urls')),
    path('', views.home,name='Home'),

]
