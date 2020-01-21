import requests
from django.shortcuts import render
from bs4 import BeautifulSoup
from requests.compat import quote_plus
from . import models


BASE_CRAIGLIST_URL = 'https://toronto.craigslist.org/search/?query={}'
# Create your views here.
def home(request):
	return render(request,'base.html')

def new_search(request):
	search = request.POST.get('search')
	final_url = BASE_CRAIGLIST_URL.format(quote_plus(search))
	response = requests.get(final_url)
	soup = BeautifulSoup(data, features = 'html.parser')
	post_titles = soup.find_all('a', {'class' : 'result-title'})
	
	data = response.text
	stuff_for_frontend = {

	'search':search,
	
	}
	return render(request, 'my_app/new_search.html')