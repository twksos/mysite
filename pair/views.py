from django.http import HttpResponse
from django.shortcuts import render_to_response, redirect
from django.template.context import RequestContext
from mysite.pair.models import Programmer

def index(request):
    return render_to_response('pair/index.html',{'all_programmers':Programmer.objects.all},context_instance=RequestContext(request))

def get_pair_table(request):
    return render_to_response('pair/pair_table.html',{'all_programmers':Programmer.objects.all})

def do_pair(request,programmer_0_id,programmer_1_id):
    programmer_0=Programmer.objects.get(id=programmer_0_id)
    programmer_1=Programmer.objects.get(id=programmer_1_id)
    programmer_0.pair_with(programmer_1)
    return HttpResponse('<div class="message success">'+programmer_0.name+' and '+programmer_1.name+' paired.</div>')

def new_programmer(request):
    if request.POST:
        if request.POST['new_programmer_name'] !='':
            Programmer(name=request.POST['new_programmer_name']).save()
            return redirect('/pair/')
        else:
            msg = 'Error:programmer name needed'
            return render_to_response('pair/index.html',{'all_programmers':Programmer.objects.all,'error_message':msg},context_instance=RequestContext(request))

def process_programmer(request,programmer_id):
    if request.method=='DELETE':
        programmer = Programmer.objects.get(id=programmer_id)
        success_msg = 'programmer '+programmer.name+' deleted.'
        programmer.delete()
        return HttpResponse('<div class="message success">'+success_msg+'</div>')