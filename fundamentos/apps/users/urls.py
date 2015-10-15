from django.conf.urls import url

from .views import LogInView, UserRegisterView

urlpatterns = [
	url(r'^ingresar/$', LogInView.as_view(), name='login'),
	url(r'^registrar/$', UserRegisterView.as_view(), name='register'),
]
