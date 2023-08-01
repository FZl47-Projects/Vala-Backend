from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('manager/',include('manager.urls')),
    path('azmayesh/',include('azmayesh.urls')),
    path('comment/',include('comment.urls')),
    path('post/',include('post.urls')),
    path('ravand/',include('ravand.urls')),
    path('routin/',include('routin.urls')),
    path('routin/',include('routin.urls')),
    path('story/',include('story.urls')),
    path('ticket/',include('ticket.urls')),
    path('user/',include('user.urls')),
    path('program/',include('program.urls')),
    path('reserve/',include('reserve.urls')),
    path('cortex/',include('cortex.urls')),
    path('chat/',include('chat.urls')),
    path('store/',include('store.urls')),
    path('analyze/',include('analyze.urls')),
    
]
urlpatterns +=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)