from django.shortcuts import render
from firstapp.models import Student

# Create your views here.
def studentview(request):
    std_list=Student.objects.all()
    print(std_list)
    std_dict={'std_list':std_list}
    return render(request,'firstapp/app.html',context=std_dict)