from django.http import HttpResponsePermanentRedirect
from django.urls import reverse
from django.shortcuts import render
from django.views import View

from .models import Student
from .forms import StudentForm

# Create your views here.
'''
def index1(request):
    #students = Student.objects.all()
    students = Student.get_all()
    return render(request,'index1.html',context={'students':students})

def index(request):
    students = Student.objects.all()
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponsePermanentRedirect(reverse('index'))
    else:
        form = StudentForm()
    context = {'students':students,'form':form,}
    return render(request,'index.html',context=context)
'''

class IndexView(View):
    template_name = 'index.html'

    def get_context(self):
        students = Student.get_all()
        context = {'students':students,}
        return context
    def get(self,request):
        context = self.get_context()
        form = StudentForm()
        context.update({'form':form})
        return render(request,self.template_name,context=context)
    def post(self,request):
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponsePermanentRedirect(reverse('index'))
        context = self.get_context()
        context.update({'form':form})
        return render(request,self.template_name,context=context)