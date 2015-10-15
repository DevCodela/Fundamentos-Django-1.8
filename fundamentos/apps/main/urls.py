from django.conf.urls import url
# from . import views
from .views import Home

urlpatterns = [
	# url(r'^$', views.home, name="home"),
	url(r'^$', Home.as_view(), name="home"),
]
