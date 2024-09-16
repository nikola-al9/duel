from django.shortcuts import render

def register_view(request):
    return render(request, 'register.html')

def main_menu_view(request):
    return render(request, 'main_menu.html')

def login_view(request):
    return render(request, 'login.html')

def registration_with_token_view(request):
    return render(request, 'registration_with_token.html')
