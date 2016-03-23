# line 3 and 4 for forms

from django.shortcuts import render, render_to_response, redirect
from django.template import RequestContext
from main.models import State, StateCapital, City
from django.http import HttpResponse
from django.views.generic import ListView
from django.views.generic import DetailView
from django.contrib.auth.decorators import login_required

from main.forms import CitySearchForm, CreateCityForm, CityEditForm


# Create your views here.

@login_required
def city_delete(request, pk):

	City.objects.get(pk=pk).delete()

	return redirect('/city_list/')

@login_required
def city_edit(request, pk):
	request_context = RequestContext(request)
	context = {}

	city = City.objects.get(pk=pk)

	context['city'] = city

	form = CityEditForm(request.POST or None, instance=city)
	print request.POST
	context ['form'] = form
	print form.is_valid()
	if form.is_valid():
		form.save()

		return redirect('/state_list/')

	return render_to_response('city_edit.html', context, context_instance=request_context)





def city_create(request):
	request_context = RequestContext(request)
	context = {}

	if request.method == 'POST':
		form = CreateCityForm(request.POST)
		context['form'] = form

		if form.is_valid():
			form.save()
			return render_to_response('city_create.html', context, context_instance=request_context)
		else:
			context['valid'] = form.errors
			return render_to_response('city_create.html', context, context_instance=request_context)
	else:
		form = CreateCityForm()
		context['form'] = form
		

		return render_to_response('city_create.html', context, context_instance=request_context)


def city_search(request):
	request_context = RequestContext(request)

	context = {}

	if request.method == 'POST':
		form = CitySearchForm(request.POST)
		context['form'] = form

		print 'post'

		if form.is_valid():
			name = "%s" % form.cleaned_data['name']
			state = form.cleaned_data['state']

			print 'is valid'
			print name
			print state

			context['city_list'] = City.objects.filter(name__startswith=name, state__name__startswith=state)

			print context['city_list']


			return render_to_response('city_search.html', context, context_instance=request_context)

		else:
			context['valid'] = form.errors

			print 'errors'

			return render_to_response('city_search.html', context, context_instance=request_context)
	else:
		form = CitySearchForm()
		context['form'] = form
		return render_to_response('city_search.html', context, context_instance=request_context)

def state_detail(request, id):
	state = State.objects.get(id=id)
	return HttpResponse(state)	

def state_list(request):
	states = State.objects.all()

	state_list = []

	for state in states:
		try:
			state_list.append("<a href='/state_detail/%s'> %s -- %s</a> <br>" % (state.id, state.name, state.statecapital.name))
		except Exception, e:
			print e
			print state.name
			print state.id
			State.objects.get(id=state.id).delete()
	return HttpResponse(state_list)

class StateListView(ListView):
	model = State
	template_name = 'state_list.html'
	context_object_name = 'states'

class StateDetailView(DetailView):
	model = State
	template_name = 'state_detail.html'
	context_object_name = 'state'


def search_cities(request):
	get_var = request.GET.get('q', None)

	text_string = ''
	if get_var != None:
		text_string += 'Search term : %s <br>' % get_var

	text_string += """
	<form action="/search_cities/" method="GET">

	Seach cities :
	<input type="text" name="q">
	<br>
	<input type="submit" value="SEARCH">
	</form>
	"""

	if get_var != None:
		cities = City.objects.filter(name__icontains=get_var)
		for city in cities:
			text_string +='city name : %s | state : %s<br>' % (city.name, city.state.name)
	return HttpResponse(text_string)


def template_view(request):
	
	context = {}
	
	states = State.objects.all()

	context['states'] = states

	return render(request, 'state_list.html', context)

def detail_view(request, name):
	context = {}

	state = State.objects.get(name=name)

	context['state'] = state

	return render(request, 'state_detail.html', context)


