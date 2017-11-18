from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^api/chart/data/$', views.ChartData.as_view()),
    url(r'^results$', views.results, name='results'),
]