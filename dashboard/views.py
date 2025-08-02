from django.shortcuts import render
from django.http import JsonResponse
from pymongo import MongoClient


import os

client = MongoClient(os.getenv("MONGO_URI"))
db = client['intern_portal']
collection = db['interns']


def index(request):
    return render(request, 'dashboard/index.html')

def dashboard(request):
    return render(request, 'dashboard/dashboard.html')

def leaderboard(request):
    return render(request, 'dashboard/leaderboard.html')

def api_intern(request):

    intern = collection.find_one({})
    if intern:
        data = {
            'name': intern.get('name'),
            'referral_code': intern.get('referral_code'),
            'donations_raised': intern.get('donations_raised'),
        }
        print(data)
    else:
        data = {
            'name': 'No intern found',
            'referral_code': 'N/A',
            'donations_raised': 0
        }
    return JsonResponse(data)
