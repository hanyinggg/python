from django.shortcuts import render,get_object_or_404
from django.views import generic
from django.urls import reverse
from .models import Heros, Items, Skills


class IndexView(generic.ListView):
	context_object_name = 'hero_list'
	template_name = 'dota2_data/index.html'
	def get_queryset(self):
		return Heros.objects.order_by('id')


class DetailView(generic.DetailView):
 	model = Heros
 	template_name = 'dota2_data/detail.html'





# Create your views here.
