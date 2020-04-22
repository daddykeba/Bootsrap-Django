from django.conf.urls import url
from frist_app import views

# TEMPLATE TAGGIND
app_name = 'frist_app'

urlpatterns = [
	url(r'^relative$', views.relative, name="relative"),
	url(r'^other$', views.other, name="other"),
	url(r'^base$', views.base, name="base"),
    url(r'^$', views.index, name="index"),
    url(r'^formpage$', views.form_name_view, name="form_name"),
]