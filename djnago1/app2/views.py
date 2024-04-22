from django.shortcuts import render
from django.http import JsonResponse
from app2.forms import selection

def home(request):
    form = selection()  # Instantiate form by default
    if request.method == "POST":
        form = selection(request.POST)
    return render(request, 'app2/index.html', {"form": form})


def get_number(request):
    if request.method == "POST":
        form = selection(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            even = [i for i in range(0, data['select']+1, 2)]
            odd = [i for i in range(0, data['select']+1, 1) if i % 2 == 1]
            result = list(zip(odd, even))
            return JsonResponse({'param1': result})
        else:
            return JsonResponse({'error': 'Form data is invalid'}, status=400)
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)
