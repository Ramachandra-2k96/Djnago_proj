from django.urls import path
from app2.views import home,get_number
urlpatterns = [
	path('', home),
 	path('get', get_number),
 ]