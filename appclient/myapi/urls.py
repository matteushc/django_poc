from django.urls import include, path
from django.contrib import admin
from rest_framework import routers
from django.views.generic.base import TemplateView
from django.contrib.auth.decorators import login_required
from . import views

router = routers.DefaultRouter()
router.register(r'appclient', views.AppClientViewSet)


urlpatterns = [
    path('rest/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('buscar/', login_required(views.AppClientView.as_view(), login_url='login'), name='buscar'),
    path('buscar_log/', views.your_view, name='buscar_log'),
    path("admin/", admin.site.urls),
    path("accounts/", include("django.contrib.auth.urls")),
    path("", login_required(TemplateView.as_view(template_name="home.html"), login_url='login/'), name="home"),
    path('upload/', views.upload_file, name='upload_file'),
    path('login/', views.LoginView.as_view(), {'template_name': 'login.html'}, name='login'),
]