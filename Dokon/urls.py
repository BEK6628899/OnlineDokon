from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from Asosiy.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Home2View.as_view()),
    path('Asosiy/',include('Asosiy.urls')),
    path('Buyurtma/',include('Buyurtma.urls')),
    path('User/',include('User.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


