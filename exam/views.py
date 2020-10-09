from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from exam.models import Student
import json

# Create your views here.
def index(request):
	peo=Student.objects.all()
	tab={'peo':peo}
	return render(request,"exam/index.html",tab)

def check(request):
    name = request.GET.get('ser', None)
    data = {
        'is_taken': Student.objects.filter(name=name).exists()
    }
    return JsonResponse(data)