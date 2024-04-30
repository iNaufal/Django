from django.contrib import admin
from django.urls import path, include

#pemanggilan views, 3 deklarasi
from . import views
from blog import views as blogviews
from contact import views as contactviews
# from . views import index, blog
# from . views import *

urlpatterns = [
    path('', views.index),
    path('blog/', include('blog.urls')),
    path('contact/', include('contact.urls')),
    path('admin/', admin.site.urls),
]
