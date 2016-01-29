from django.shortcuts import render
from django.views.generic import TemplateView

from .models import Category, Payment, City, Restaurant
# Create your views here.
class IndexView(TemplateView):

	template_name = 'index.html'
	def get_context_data(self, **kwargs):
		context = super(IndexView, self).get_context_data(**kwargs)
		context['categories'] = Category.objects.all()
		context['payments'] = Payment.objects.all()
		context['cities'] = City.objects.all()
		context['restaurants'] = Restaurant.objects.all()
		return context