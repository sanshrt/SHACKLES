from django.shortcuts import render, redirect
from .forms import AccommodationForm
from django.contrib.auth.decorators import login_required  # Ensure user is logged in

@login_required
def accommodation_view(request):
    if request.method == "POST":
        form = AccommodationForm(request.POST)
        if form.is_valid():
            accommodation = form.save(commit=False)
            accommodation.user = request.user  # Assign the logged-in user
            accommodation.save()
            return redirect('home')  # Redirect to a success page
    else:
        form = AccommodationForm()
    
    return render(request, 'add_accommodation.html', {'form': form})
