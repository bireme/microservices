from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from rest_framework import routers

from main import views as api_views

router = routers.DefaultRouter()
router.register(r'topic', api_views.TopicQueryViewSet)

admin.site.site_header = 'IAHX Topic Query'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),

    # redirect first page for /api/
    path('', RedirectView.as_view(url='/api/', permanent=True))
]
