import csv

from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse

from pagination import settings


def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    bus_stations = []

    with open(settings.BUS_STATION_CSV, newline='') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=',')
        for row in reader:
            bus_stations.append(
                {
                    "Name": row['Name'],
                    "Street": row['Street'],
                    "District": row['District']
                }
            )

    paginator = Paginator(object_list=bus_stations, per_page=10)
    current_page = request.GET.get('page', 1)
    page = paginator.get_page(current_page)

    # получите текущую страницу и передайте ее в контекст
    # также передайте в контекст список станций на странице

    context = {
        'bus_stations': page.object_list,
        'page': page
    }
    return render(request, 'stations/index.html', context)
