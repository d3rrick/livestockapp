
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404, HttpResponse
from django.core.serializers import serialize
from django.template.context import RequestContext
from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate, login
from django.core.context_processors import csrf
from django.core.mail import send_mail
from django.shortcuts import render_to_response, render, get_object_or_404, HttpResponseRedirect
from liveapp.models import *
from liveapp.forms import *
from liveapp.serializers import *
from django.contrib import messages
from django.contrib.auth.models import User
from django.conf import settings

from django.utils import timezone
import hashlib
import datetime
import random
from rest_framework import status

from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from africastalking.AfricasTalkingGateway import (AfricasTalkingGateway, AfricasTalkingGatewayException)


import json


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'],
                                password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('Authenticated '
                                        'successfully')
            else:
                return HttpResponse('Disabled account')
        else:
            return HttpResponse('Invalid login')
    else:
        form = LoginForm()
    return render(request, 'green/login.html', {'form': form})


def maps(request):
    return render(request, 'liveapp/maps.html', {})


def home(request):
    form = RegistrationForm()
    form2 = IncidenceForm()
    context = {'form': form,
               'form2': form2}
    return render(request, 'green/index.html', context)


def incidence(request):
    form = IncidenceForm()
    if request.method == 'POST':
        form = IncidenceForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            # return index(request)
#            return HttpResponseRedirect(reverse("incident"))
        else:
            print form.errors
    else:
        form = IncidenceForm()
    return render(request, 'green/incidence_form.html', {'form': form})


def portal(request):
    return render(request, 'liveapp/portal.html', {})


class CorridorList(APIView):

    def get(self, request):
        corridor = Corridor.objects.all()
        serializer = CorridorSerializer(corridor, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = CorridorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class IncidenceList(APIView):

    def get(self, request):
        incidences = Incidence.objects.all()
        serializer = IncidenceSerializer(incidences, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = IncidenceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def town_data(request):
    towns = serialize('geojson', Town.objects.all())
    return HttpResponse(towns, content_type='json')


def corridors(request):
    corridor = serialize('geojson', Corridor.objects.all())
    return HttpResponse(corridor, content_type='json')


def facility_data(request):
    facility = serialize('geojson', Facility.objects.all())
    return HttpResponse(facility, content_type='json')


def incidence_data(request):
    incidence = serialize('geojson', Incidence.objects.all())
    return HttpResponse(incidence, content_type='json')


def cattle_data(request):
    cattle = serialize('geojson', Cattle.objects.all())
    return HttpResponse(cattle, content_type='json')


def goat_data(request):
    goat = serialize('geojson', Goat.objects.all())
    return HttpResponse(goat, content_type='json')


def sheep_data(request):
    sheep = serialize('geojson', Sheep.objects.all())
    return HttpResponse(sheep, content_type='json')


def poultry_data(request):
    poultry = serialize('geojson', Poultry.objects.all())
    return HttpResponse(poultry, content_type='json')


def market_data(request):
    market = serialize('geojson', Market.objects.all())
    return HttpResponse(market, content_type='json')


def event_data(request):
    event = serialize('geojson', Event.objects.all())
    return HttpResponse(event, content_type='json')


def subcounty_data(request):
    subcounties = serialize('geojson', Subcounty.objects.all())
    return HttpResponse(subcounties, content_type='json')


def charts(request):
    incidences = Incidence.objects.all()
    markets = Market.objects.all()
    inciddata = serialize('json', incidences)
    marketdata = serialize('json', markets)

    return render(request, 'liveapp/charts.html', {'inciddata': inciddata, 'marketdata': marketdata})


@csrf_exempt
def sms(request):
    res = {}
    nos = []

    if request.is_ajax():
        points = request.POST
        thisdict = json.loads(points.get('arr'))
        # print thisdict

        for line in thisdict:
            res.update(line)
            nos.append(res['farmer_telephone'])
    x = ",".join(nos)
    print "x is {}".format(x)

    username = "deryqm"
    apikey = "6ee711cfda7e14a74882f0ad4fc864f861f69eafe0c9effa8e61db27e9b7f03b"
    to = x
    message = "hello, This is to inform you that there is a severe cow disease called anthrax that has been reported near your farm, please ensure your animals are vaccinated #livestockapp"
    gateway = AfricasTalkingGateway(username, apikey, "deryqm")
    try:
        results = gateway.sendMessage(to, message)

        for recipient in results:
            print 'number=%s;status=%s;messageId=%s;cost=%s' % (recipient['number'],
                                                                recipient['status'],
                                                                recipient['messageId'],
                                                                recipient['cost'])
    except AfricasTalkingGatewayException, e:
        print 'Encountered an error while sending: %s' % str(e)
