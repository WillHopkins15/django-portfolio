from django.shortcuts import render, get_object_or_404, redirect
from .models import Cv
from .forms import CvForm

def cv_view(request):
    cv = get_object_or_404(Cv, pk=1)
    return render(request, 'cv/cv_view.html', {'cv': cv})

def cv_edit(request):
    cv = get_object_or_404(Cv, pk=1)
    if request.method == "POST":
        form = CvForm(request.POST, instance=cv)
        if form.is_valid():
            cv = form.save(commit=False)
            cv.save()
            return redirect('cv_view')
    else:
        form = CvForm(instance=cv)
    return render(request, 'cv/cv_edit.html', {'form': form})   