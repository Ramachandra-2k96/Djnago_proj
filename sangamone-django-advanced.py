import os
dproject=input("Enter the django project name: ")
dapp=input("Enter the django app name: ")
print("basic - 1\nfactorial - 2\nform - 3")
dexm=int(input("Enter the number of example: "))
os.chdir(dproject)
os.chdir(f"./{dproject}")
f1=open("settings.py","r+")
info1=f1.read()
if f"{dapp}'," not in info1:
    a=info1.replace("'django.contrib.staticfiles',",f"'django.contrib.staticfiles',\n\t'{dapp}',")
    f1.seek(0)
    f1.write(a)
f1.close()

f1=open("urls.py","r+")
info1=f1.read()
if f"{dapp}.urls" not in info1 and "from django.urls import path,include" not in info1:
    any1=info1.replace("path('admin/', admin.site.urls),",f"""path('admin/', admin.site.urls),\n\tpath("{dapp}/" ,include("{dapp}.urls")),""").replace("from django.urls import path","from django.urls import path,include")
    f1.seek(0)
    f1.write(any1)
elif f"""path('admin/', admin.site.urls),\n\tpath("{dapp}/" ,include("{dapp}.urls")),""" not in info1:
    any1=info1.replace("path('admin/', admin.site.urls),",f"""path('admin/', admin.site.urls),\n\tpath("{dapp}/" ,include("{dapp}.urls")),""")
    f1.seek(0)
    f1.write(any1)
f1.close()

os.chdir(f"../{dapp}")

f1=open("views.py","w")
any=""
if dexm==1:
    any="""from django.shortcuts import render
def home(request):
    return render(request,'"""+dapp+"""/index.html',{'param1':"hello world"})"""
elif dexm==2:
    any=f"""from django.shortcuts import render
def home(request):
    result=1
    n1=5
    for i in range(1,n1+1,1):
        result=result*i
    return render(request,'"""+dapp+"""/index.html',{'param1':result,'param2':n1})"""
elif dexm==3:
    any="""from django.shortcuts import render
from """+dapp+""".forms import inputform
def home(request):
    result = None
    n1 = None
    if request.method=="POST":
        form1=inputform(request.POST)
        if form1.is_valid():
            data=form1.cleaned_data
            n1=data.get("input")
            result=fact(n1)
            return render(request,\""""+dapp+"""/index.html",{'param1':result, 'param2':n1, 'form':form1})
    else:
        form1=inputform()  
    return render(request,\""""+dapp+"""/index.html",{'param1':result, 'param2':n1, 'form':form1})
def fact(n1):  
    result=1
    for i in range(1,n1+1,1):
        result=result*i
    return result"""
f1.write(any)
f1.close()

if os.path.exists('forms.py')==False:
    open('forms.py','w')
f1=open('forms.py','w')
f1.write("""from django import forms
class inputform(forms.Form):
    name=forms.CharField(max_length=10)
    input=forms.IntegerField(min_value=1,max_value=200,label="$3")""")
f1.close()

if os.path.exists('urls.py')==False:
    open('urls.py','w')
f1=open("urls.py","r+")
if "urlpatterns = [" not in f1.read():
    f1.write(f"from django.urls import path\nfrom {dapp}.views import home\nurlpatterns = [\n\tpath('', home),]")
else:
    a=f1.read().replace("urlpatterns = [",f"urlpatterns = [\n\tpath('', home),").replace("from django.urls import path",f"from django.urls import path\nfrom {dapp}.views import home")
    f1.seek(0)
    f1.write(a)
f1.close()

if os.path.exists(f"templates/{dapp}")==False:
    os.makedirs(f"templates/{dapp}")
os.chdir(f"templates/{dapp}")
f1=open("index.html","w")
if dexm==1:
    f1.write("""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <p>Hello World</p>
    <p>The factorial of {{param1}} is {{param2}}</p>
</body>
</html>""")

elif dexm==2:    
    f1.write("""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <p>Hello World</p>
    <p>{{param1}}</p>
</body>
</html>
""")

elif dexm==3:
    f1.write("""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <h1>Factorial Program</h1>
    <form method="POST">
    {% csrf_token %}
    {{form.as_p}}    
    <button type="submit">find factorial</button>
    </form>
    {% if param1 %}
    <h2>Factorial of {{param2}} is {{param1}}</h2>
    {% endif %}
</body>
</html>""")
f1.close()

