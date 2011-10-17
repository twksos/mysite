# Create your views here.
from datetime import datetime
from django.http import HttpResponse
from django.template import loader
from django.template.context import Context
from models import Pair
from mysite.pair.models import Programmer

def prepare_data(request):
    for programmer in Programmer.objects.all():
        programmer.delete()
    programmer_ada = Programmer(name='ada')
    programmer_ada.save()
    programmer_van = Programmer(name='van')
    programmer_van.save()
    programmer_zoi = Programmer(name='zoi')
    programmer_zoi.save()
    pair_record1 = Pair(programmer_0=programmer_ada, programmer_1=programmer_van, date=datetime.now())
    pair_record1.save()
    pair_record2 = Pair(programmer_0=programmer_ada, programmer_1=programmer_zoi, date=datetime.now())
    pair_record2.save()
    pair_record3 = Pair(programmer_0=programmer_ada, programmer_1=programmer_van, date=datetime.now())
    pair_record3.save()
    return HttpResponse('data created. <a href="/pair">start</a>')


def create_pair_table_title(programmers):
    pair_table = '<tr><th width=150 align=left>names</th>'
    for programmer_0 in programmers:
        pair_table += '<th width=150 align=left>' + programmer_0.name + '</th>'
    pair_table += '</tr>'
    return pair_table


def create_pair_table_body(programmers):
    pair_table_body = ''
    for programmer_0 in programmers:
        pair_table_body += '<tr><td>' + programmer_0.name + '</td>'
        for programmer_1 in programmers:
            if programmer_0==programmer_1:
                pair_table_body += '<td>X</td>'
                break
            else:
                pair_table_body += '<td><a href="/pair/do_pair/'+str(programmer_0.id)+'/'+str(programmer_1.id)+'/">' + str(programmer_0.pair_time_with(pair=programmer_1)) + '</a></td>'
        pair_table_body += '</tr>'
    return pair_table_body


def index(request):
    all_programmers = Programmer.objects.all()
    template = loader.get_template('pair/index.html')
    pair_table = '<table border=1 align=left>'
    pair_table += create_pair_table_title(all_programmers)
    pair_table += create_pair_table_body(all_programmers)
    pair_table += '</table>'

    context = Context({
        'pair_table': pair_table,
        })
    return HttpResponse(template.render(context))

def do_pair(request,programmer_0_id,programmer_1_id):
    programmer_0=Programmer.objects.get(id=programmer_0_id)
    programmer_1=Programmer.objects.get(id=programmer_1_id)
    programmer_0.pair_with(programmer_1)
    return index(request)

def new_programmer(request,programmer_name):
    Programmer(name=programmer_name).save()
    return HttpResponse(programmer_name+' created. <a href="/pair">start</a>')