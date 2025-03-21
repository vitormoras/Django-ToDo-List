from django.shortcuts import render, redirect
from .models import Tarefa
from .forms import TarefaForm
from django.contrib import messages


# Create your views here.
def index(request):
    tarefa = Tarefa.objects.all()
    if request.method == 'POST':
        form = TarefaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Tarefa foi adicionada com sucesso!')
            return redirect('index')

    form = TarefaForm()
    contexto = {
        'tarefas':tarefa,
        'form':form,
    }
    return render(request, 'index.html', contexto,)


def excluir_tarefa(request, id):
    tarefa = Tarefa.objects.get(id=id)
    tarefa.delete()
    return redirect('index')