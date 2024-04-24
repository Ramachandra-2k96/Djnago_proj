from django.shortcuts import render
def home(request):
    nums=[]
    chrs=[]
    result1=[]
    for i in range(65,65+26,1):
        nums.append(i)
        chrs.append(chr(i))
    result1=zip(nums, chrs)
    return render(request,'app3/index.html',{'param2':result1})