
from django.contrib import admin
from django.urls import path, include
from django.contrib.staticfiles.urls import static, staticfiles_urlpatterns
from django.conf import settings
from App_Posts import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.Home_View, name = 'home'),
    path('account/', include('App_Login.urls')),
    path('posts/', include('App_Posts.urls')),
]


urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
