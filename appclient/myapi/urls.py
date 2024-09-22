from django.urls import include, path
from django.contrib import admin
from rest_framework import routers
from django.views.generic.base import TemplateView
from django.contrib.auth.decorators import login_required
from . import views

router = routers.DefaultRouter()
router.register(r'appclient', views.LogsViewSet)


urlpatterns = [
    #path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('buscar/', login_required(views.LogsView.as_view(), login_url='/'), name='buscar'),
    path('buscar_log/', views.your_view, name='buscar_log'),
    path("admin/", admin.site.urls),
    path("accounts/", include("django.contrib.auth.urls")),
    path("", TemplateView.as_view(template_name="home.html"), name="home"),
    path('upload/', views.upload_file, name='upload_file'),
]