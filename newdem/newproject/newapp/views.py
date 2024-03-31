from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Report, Point, Bonus, Merchandise, Redemption

# Create your views here.
def home(request):
    return render(request, 'newapp/home.html')


@login_required
def submit_report(request):
    if request.method == 'POST':
        description = request.POST.get('description')
        report = Report.objects.create(user=request.user, description=description)
        # Award points to the user for submitting a report
        point, created = Point.objects.get_or_create(user=request.user)
        point.amount += 10  # Award 10 points for each report
        point.save()
        messages.success(request, 'Report submitted successfully.')
        return redirect('profile')
    return render(request, 'newapp/submit_report.html')

@login_required
def profile(request):
    user = request.user
    points = Point.objects.get(user=user).amount
    bonuses = Bonus.objects.get(user=user).amount
    return render(request, 'newapp/profile.html', {'points': points, 'bonuses': bonuses})

@login_required
def merchandise(request):
    merchandise_list = Merchandise.objects.all()
    return render(request, 'newapp/merchandise.html', {'merchandise_list': merchandise_list})

@login_required
def redeem_points(request, merchandise_id):
    merchandise = Merchandise.objects.get(pk=merchandise_id)
    user_points = Point.objects.get(user=request.user).amount

    if user_points >= merchandise.points_required:
        # Deduct points from the user
        point = Point.objects.get(user=request.user)
        point.amount -= merchandise.points_required
        point.save()
        # Record redemption
        redemption = Redemption.objects.create(user=request.user, merchandise=merchandise)
        messages.success(request, 'Merchandise redeemed successfully.')
    else:
        messages.error(request, 'Insufficient points to redeem this merchandise.')

    return redirect('merchandise')
