from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse_lazy
from horarios.forms import Asighorarioform, Asuetoform
from horarios.models import*
from datetime import datetime

# Create your views here.
@login_required
def menu_horarios(request):
    return render(request,'horarios/menuhorario.html')
@login_required
def listrangohoras(request):
    listrangohoras=RangoHora.objects.all()
    return render (request,'horarios/listrangohoras.html',{'listarango':listrangohoras})
@login_required
def regrangohoras(request):
    if request.method=='POST':
        hi=request.POST['hi']
        hf=request.POST['hf']
        ran=request.POST['rango']
        RangoHora.objects.create(rango_hora=ran,hora_inicio=hi,hora_fin=hf)
        return redirect('listrangohoras')
@login_required
def editarhoras(request,id):
    editarhoras=RangoHora.objects.get(id=id)
    return render (request,'horarios/editarhoras/editarhoras.html',{'ed':editarhoras})
@login_required
def actualizarhoras(request):
    if request.method=='POST':
        id=request.POST['id']
        hi=request.POST['hi']
        hf=request.POST['hf']
        ran=request.POST['rango']
        RangoHora.objects.filter(id=id).update(rango_hora=ran,hora_inicio=hi,hora_fin=hf)
        return redirect('listrangohoras')
@login_required
def regtipohorarios(request):
    listartipohorarios= TipoHorario.objects.all()
    if request.method=='POST':
        t=request.POST['t']
        TipoHorario.objects.create(descripcion=t)
    return render (request,'horarios/regtipohorario/regtipohorarios.html',{'lista':listartipohorarios})
@login_required
def editartipohorarios(request,id):
    editartipohorario=TipoHorario.objects.get(id=id)
    return render(request,'horarios/editartipohorario/editartipohorario.html',{'ed':editartipohorario})

@login_required
def actualizartipohorario(request):
    if request.method=='POST':
        id=request.POST['id']
        t=request.POST['t']
        TipoHorario.objects.filter(id=id).update(descripcion=t)
        return redirect('regtipohorario')
@login_required
def listhorarios(request):
    thorarios=TipoHorario.objects.all()
    lishorarios=Horario.objects.all()
    if request.method=='POST':
        t=request.POST['t']
        d=request.POST['d']
        Horario.objects.create(descripcion=d,tipohorario_id=t)
    return render(request, 'horarios/listhorario/listhorario.html', {'thorarios':thorarios,'lista':lishorarios})
@login_required
def editarhorarios(request,id):
    editarhorario=Horario.objects.get(id=id)
    thorario=TipoHorario.objects.all()
    return render(request,'horarios/editarhorario/editarhorario.html',{'editar':editarhorario,'thorarios':thorario})
@login_required
def actualizarhorario(request):
    if request.method=='POST':
        id=request.POST['id']
        d=request.POST['d']
        t=request.POST['t']
        Horario.objects.filter(id=id).update(descripcion=d,tipohorario_id=t)
        return redirect('listhorario')
@login_required
def listurno(request):
    h=Horario.objects.all()
    turno=Turno.objects.all()
    return render (request,'horarios/listurnos/listarturnos.html', {'h':h,'turno':turno.order_by('horario')})

@login_required
def regturno(request,id):
    h=id   
    t=Turno.objects.filter(horario=h)
    r=RangoHora.objects.all()
    return render(request,'horarios/regturno/regturno.html',{'h':h,'t':t,'r':r})
@login_required
def guardarturno(request):
    if request.method=='POST':
        ho=request.POST['h']
        d=request.POST['d']
        rr=request.POST['r']
        Turno.objects.create(dia=d,horario_id=ho,rango_hora_id=rr)
        return redirect('regturno/'+ho)
@login_required
def editarturno(request,id):
    t=Turno.objects.get(id=id)
    r=RangoHora.objects.all()
    h=Horario.objects.all()
    return render(request,'horarios/editarturno/editarturno.html',{'t':t,'r':r,'h':h})
@login_required
def actualizarturno(request):
    if request.method=='POST':
        id=request.POST['id']
        d=request.POST['d']
        h=request.POST['h']
        r=request.POST['r']
        Turno.objects.filter(id=id).update(dia=d,horario_id=h,rango_hora_id=r)
        return redirect('listurno')
@login_required
def listasignarhorario(request):
    lista=AsigHorario.objects.all()
    

    return render(request,'horarios/listasighorarios/listasighorarios.html',{'lista':lista})
@login_required
class AsignarhorarioDetail(DetailView):
    model=AsigHorario

@login_required
class AsighorarioUpdate(SuccessMessageMixin,UpdateView):
    model=AsigHorario
    form_class=Asighorarioform
    success_url = reverse_lazy('listasignarhorarios')
    success_message = "Actualizacion realizada exitosamente!"
@login_required
def asignarhorario(request):
    #asignacion de horario creada
    em=Empleado.objects.all()
    h=Horario.objects.all()
    if request.method=='POST':
        now = datetime.now()
        fereg=now.strftime('%Y-%m-%d')
        usu_reg=request.POST['usu_reg']
        f1=request.POST['f1']
        f2=request.POST['f2']
        ho=request.POST['ho']
        empleado=request.POST['em']
        AsigHorario.objects.create(fecha_inicio=f1,fecha_fin=f2,fecha_registro=fereg,usuario_registro=usu_reg,empleado_id=empleado,horario_id=ho)
    return render(request,'horarios/asignarhorarios/asignarhorarios.html',{'em':em,'h':h})
@login_required
def AsuetoList(request):
    now = datetime.now()
    fereg=now.strftime('%Y')
    lista=Asueto.objects.filter(fecha_inicio__year=fereg)
    return render(request, 'horarios/asueto_list.html',{'object_list':lista})
@login_required
class AsuetoCreate(CreateView,SuccessMessageMixin):
    model=Asueto
    form_class=Asuetoform
    success_url=reverse_lazy('asuetolist')
    success_message="Registro creado satisfactoriamente"
@login_required
class AsuetoDetail(DetailView):
    model=Asueto
@login_required
class AsuetoUpdate(UpdateView, SuccessMessageMixin):
    model=Asueto
    form_class=Asuetoform
    success_url=reverse_lazy('asuetolist')
    success_message="Actualizacion realizada satisfactoriamente"