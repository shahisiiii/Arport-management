from django.shortcuts import render, redirect
from .forms import AirportForm
from .models import Airport

def airport_create_view(request):
    if request.method == 'POST':
        form = AirportForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('airport_list')  # Redirect to list view after success
    else:
        form = AirportForm()
    return render(request, 'airport_form.html', {'form': form})


def airport_list_view(request):
    airports = Airport.objects.all()
    return render(request, 'airport_list.html', {'airports': airports})



from django.shortcuts import render
from .forms import FindLastChildForm
from .models import Airport

def find_last_child_airport(request):
    result = None
    level = 0

    if request.method == 'POST':
        form = FindLastChildForm(request.POST)
        if form.is_valid():
            current_airport = form.cleaned_data['starting_airport']
            direction = form.cleaned_data['direction']

            while True:
                try:
                    next_airport = Airport.objects.get(
                        parent_code=current_airport,
                        parent_position=direction
                    )
                    current_airport = next_airport
                except Airport.DoesNotExist:
                    break

            result = {
                'code': current_airport.code,
                'direction': 'Left' if direction == 'L' else 'Right'
            }

    else:
        form = FindLastChildForm()

    return render(request, 'find_last_child.html', {'form': form, 'result': result})


from django.shortcuts import render, get_object_or_404
from .models import Airport
from .forms import LongestDurationForm

def find_longest_duration(request):
    result = None
    if request.method == "POST":
        form = LongestDurationForm(request.POST)
        if form.is_valid():
            start_code = form.cleaned_data['start_code']
            end_code = form.cleaned_data['end_code']
            current_airport = get_object_or_404(Airport, code=end_code)
            path = []

            while current_airport and current_airport.code != start_code:
                path.append(current_airport)
                current_airport = current_airport.parent_code

            if current_airport and current_airport.code == start_code:
                path.append(current_airport)
                path = path[::-1]  # reverse to start -> end
                durations = [
                    {
                        'from': path[i].code,
                        'to': path[i+1].code,
                        'duration': path[i+1].duration or 0
                    }
                    for i in range(len(path) - 1)
                ]
                max_step = max(durations, key=lambda x: x['duration'])
                result = {
                    'path': durations,
                    'longest': max_step
                }
            else:
                form.add_error(None, "No valid path found between given airport codes.")
    else:
        form = LongestDurationForm()

    return render(request, 'find_longest_duration.html', {'form': form, 'result': result})


from django.shortcuts import render, get_object_or_404
from .forms import ShortestDurationForm
from .models import Airport

def find_shortest_duration(request):
    result = None
    if request.method == "POST":
        form = ShortestDurationForm(request.POST)
        if form.is_valid():
            start_code = form.cleaned_data['start_code']
            end_code = form.cleaned_data['end_code']
            current_airport = get_object_or_404(Airport, code=end_code)
            path = []

            while current_airport and current_airport.code != start_code:
                path.append(current_airport)
                current_airport = current_airport.parent_code

            if current_airport and current_airport.code == start_code:
                path.append(current_airport)
                path = path[::-1]  

                durations = [
                    {
                        'from': path[i].code,
                        'to': path[i+1].code,
                        'duration': path[i+1].duration or 0
                    }
                    for i in range(len(path) - 1)
                ]

                min_step = min(durations, key=lambda x: x['duration'])
                result = {
                    'path': durations,
                    'shortest': min_step
                }
            else:
                form.add_error(None, "No valid path found between the given airport codes.")
    else:
        form = ShortestDurationForm()

    return render(request, 'find_shortest_duration.html', {'form': form, 'result': result})
