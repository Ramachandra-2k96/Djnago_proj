from django.http import JsonResponse
from django.shortcuts import render
from app2.forms import selection
def home(request):
    form = selection()
    if request.method =="POST":
        form =selection(request.POST)
    return render(request,'app1/index.html',{'form':form})

def factorial(request):
    if request.method=="POST":
        form= selection(request.POST)
        if form.is_valid():
            data=form.cleaned_data
            num=data['select']
            fact=1
            for i in range(2,num+1):
                fact=fact*i
            print(fact)
            return JsonResponse({'param1':fact}, safe=False)
    else:
        return JsonResponse({'param1':'invalid'})
    
        