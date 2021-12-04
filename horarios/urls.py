from django.urls import path
from horarios import views

urlpatterns = [
        path('horarios', views.menu_horarios, name='menu_horarios'),
        path('listarangohoras',views.listrangohoras,name='listrangohoras'),
        path('regrangohoras',views.regrangohoras,name='regrangohoras'),
        path('editarhoras/<int:id>',views.editarhoras,name='editarhoras'),
        path('actualizar',views.actualizarhoras,name='actualizarhoras'),
        path('regtipohorario',views.regtipohorarios,name='regtipohorario'),
        path('editartipohorario/<int:id>',views.editartipohorarios,name='editartipohorario'),
        path('actualizartipohorario',views.actualizartipohorario,name='actualizartipohorario'),
        path('listhorario',views.listhorarios, name='listhorario'),
        path('editarhorario/<int:id>',views.editarhorarios, name='editarhorario'),
        path('actualizarhorario',views.actualizarhorario, name='actualizarhorario'),
        path('listurnos',views.listurno,name='listurno'),
        path('regturno/<int:id>',views.regturno,name='regturno'),
        path('guardarturno',views.guardarturno, name='guardarturno'),
        path('editarturno/<int:id>',views.editarturno,name='editarturno'),
        path('actualizarturno',views.actualizarturno,name='actualizarturno'),
        path('listasighorarios',views.listasignarhorario,name='listasignarhorarios'),
        path('asignarhorarios',views.asignarhorario, name='asignarhorarios'),
        path('asighorariodetail/<int:pk>',views.AsignarhorarioDetail, name='asighorariodetail'),
        path('asighorarioeditar/<int:pk>',views.AsighorarioUpdate, name='asighorarioeditar'),
        path('asuetolist', views.AsuetoList, name='asuetolist'),
        path('asuetodetail/<int:pk>',views.AsuetoDetail,name='asuetodetail'),
        path('asuetocreate', views.AsuetoCreate,name='asuetocreate'),
        path('asuetoupdate/<int:pk>',views.AsuetoUpdate,name='asuetoupdate')
        
]