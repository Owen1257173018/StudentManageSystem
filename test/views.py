from django.shortcuts import render,reverse,redirect,HttpResponseRedirect
from test.models import *
from django.views.decorators.csrf import csrf_exempt
from django.db import transaction


# Create your views here.

# @csrf_exempt
def indexStudent(request):
    flag=0
    keys=list(request.POST.keys())
    if request.method == 'POST':
        if keys[1] == 'value':
            return redirect('/'+request.POST.get('value'))
        elif keys[1] == 'delete':
            print(request.POST.get('delete'))
            Student.objects.get(Sno=request.POST.get('delete')).delete()
            return redirect('/student')
        elif keys[1] == 'insert':
            Student.objects.create(Sno=request.POST.get('Sno'),Sname=request.POST.get('Sname'),Ssex=request.POST.get('Ssex'),Sage=request.POST.get('Sage'),Sdept=request.POST.get('Sdept'))
            return redirect('/student')
        elif keys[1] == 'update':
            Student.objects.filter(Sno=request.POST.get('Sno')).update(Sno=request.POST.get('newSno'),Sname=request.POST.get('Sname'),Ssex=request.POST.get('Ssex'),Sage=request.POST.get('Sage'),Sdept=request.POST.get('Sdept'))
        elif keys[1] == 'select':
            flag=1
            search=request.POST.get('select')
            if search=='Sno':
                all_data = Student.objects.filter(Sno=request.POST.get('content'))
            elif search=='Sname':
                all_data = Student.objects.filter(Sname=request.POST.get('content'))
            elif search=='Ssex':
                all_data = Student.objects.filter(Ssex=request.POST.get('content'))
            elif search=='Sage':
                all_data = Student.objects.filter(Sage=request.POST.get('content'))
            elif search=='Sdept':
                all_data = Student.objects.filter(Sdept=request.POST.get('content'))
    if flag==0:
        all_data = Student.objects.all()
    return render(request, 'indexStudent.html', {'all_data': all_data})

def indexCourse(request):
    flag=0
    keys=list(request.POST.keys())
    if request.method == 'POST':
        if keys[1] == 'value':
            return redirect('/'+request.POST.get('value'))
        elif keys[1] == 'delete':
            print(request.POST.get('delete'))
            Course.objects.get(Cno=request.POST.get('delete')).delete()
            return redirect('/course')
        elif keys[1] == 'insert':
            Course.objects.create(Cno=request.POST.get('Cno'),Cname=request.POST.get('Cname'),Cpno=request.POST.get('Cpno'),Ccredit=request.POST.get('Ccredit'))
            return redirect('/course')
        elif keys[1] == 'update':
            Course.objects.filter(Cno=request.POST.get('newCno')).update(Cno=request.POST.get('Cno'),Cname=request.POST.get('Cname'),Cpno=request.POST.get('Cpno'),Ccredit=request.POST.get('Ccredit'))
        elif keys[1] == 'select':
            flag=1
            search=request.POST.get('select')
            if search=='Cno':
                all_data = Course.objects.filter(Cno=request.POST.get('content'))
            elif search=='Cname':
                all_data = Course.objects.filter(Cname=request.POST.get('content'))
            elif search=='Cpno':
                all_data = Course.objects.filter(Cpno=request.POST.get('content'))
            elif search=='Ccredit':
                all_data = Course.objects.filter(Ccredit=request.POST.get('content'))
    if flag==0:
        all_data = Course.objects.all()
    return render(request, 'indexCourse.html', {'all_data': all_data})

def indexSC(request):
    if request.method == 'POST':
        if request.POST.get('value') in ['student','course','sc']:
            return redirect('/'+request.POST.get('value'))

    all_data = SC.objects.all()
    return render(request, 'indexSC.html', {'all_data': all_data})


