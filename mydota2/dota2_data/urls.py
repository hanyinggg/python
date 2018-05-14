from django.urls import path
from.import views

app_name = 'dota2_data'
urlpatterns = [
	path('', views.IndexView.as_view(), name='index'),
	path('<int:pk>', views.DetailView.as_view(), name='detail'),
]
