from django.shortcuts import render, redirect
from .forms import AsistenciaForm

def registro_asistencia(request):
    if request.method == 'POST':
        form = AsistenciaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('asistencia:confirmacion')
    else:
        form = AsistenciaForm()
    
    return render(request, 'asistencia/registro.html', {'form': form})

def confirmacion(request):
    return render(request, 'asistencia/confirmacion.html')
