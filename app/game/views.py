# app/game/views.py
import requests
from django.shortcuts import render

def history_view(request):
    token = request.GET.get('token')
    headers = {'Authorization': f'Bearer {token}'}
    response = requests.get('http://localhost:8000/api/game/backend_history/', headers=headers)
    data = response.json()
    results = data.get('results', [])
    return render(request, 'history.html', {'results': results})

def leaderboard_view(request):
    token = request.GET.get('token')
    headers = {'Authorization': f'Bearer {token}'}
    response = requests.get('http://localhost:8000/api/game/backend_leaderboard/', headers=headers)
    data = response.json()
    results = data.get('results', [])
    return render(request, 'leaderboard.html', {'players': results})

