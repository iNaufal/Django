from django.contrib import admin
from django.urls import path, include

#pemanggilan views, 3 deklarasi
from . import views
from blog import views as blogviews
from contact import views as contactviews
# from . views import index, blog
# from . views import *

urlpatterns = [
    path('blog/', include('blog.urls')),
    path('contact/', contactviews.index),
    path('', views.index),
    path('admin/', admin.site.urls),
]
