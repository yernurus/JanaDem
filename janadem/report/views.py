from django.shortcuts import render, redirect
from .forms import ReportForm

def add_report(request):
    if request.method == 'POST':
        form = ReportForm(request.POST, request.FILES)
        if form.is_valid():
            report = form.save(commit=False)
            location = Location.objects.create(
                name=form.cleaned_data['location_name'],
                latitude=form.cleaned_data['latitude'],
                longitude=form.cleaned_data['longitude']
            )
            report.location = location
            report.save()
            return redirect('success')  
    else:
        form = ReportForm()
    return render(request, 'add_report.html', {'form': form})
