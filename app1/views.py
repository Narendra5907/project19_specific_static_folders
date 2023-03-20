from django.shortcuts import render

# Create your views here.
def specifi_static(request):
    return render(request,'specifi_static.html')