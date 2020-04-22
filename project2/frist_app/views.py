# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from frist_app.models import Topic, Webpage, AccessRecord
from . import forms

# Create your views here.

def index(request):
	# return HttpResponse("Hello World!!")
	webpages_list = AccessRecord.objects.order_by('date')
	date_dict = {'access_records': webpages_list}
	return render(request, 'frist_app/index.html', context=date_dict)

def form_name_view(request):
	form = forms.FormName()

	if request.method == 'POST':
		form = forms.FormName(request.POST)
		
		if form.is_valid():
			print("Succes Validation")
			print("Name "+form.cleaned_data['name'])
			print("Email "+form.cleaned_data['email'])
			print("Text "+form.cleaned_data['text'])
	return render(request, 'frist_app/form_page.html', {'form':form})

def form_topic_view(request):
	form = forms.TopicForm()

	if request.method == 'POST':
		form = forms.TopicForm(request.POST)
		
		if form.is_valid():
			form.save(commit=True)
			return index(request)
		else:
			print("Error")
	else:
		return render(request, 'frist_app/form_topic.html', {'form':form})

def other(request):
	return render(request, 'frist_app/form_topic.html')

def relative(request):
	return render(request, 'frist_app/relative_url_templates.html')

def base(request):
	return render(request, 'frist_app/base.html')
