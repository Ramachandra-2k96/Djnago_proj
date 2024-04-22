from django.urls import path
from app1.views import home,factorial
urlpatterns = [
	path('', home),
 	path('fact', factorial),
 ]