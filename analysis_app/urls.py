from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^api/barchart/data$', views.BarChartData.as_view()),
    url(r'^api/piechart/data$', views.PieChartData.as_view()),
    url(r'^results$', views.results, name='results'),
]