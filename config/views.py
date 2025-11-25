from django.shortcuts import render

def login_page(request):
    return render(request, "login.html")

def dashboard_page(request):
    return render(request, "dashboard.html")

def create_transaction_page(request):
    return render(request, "create_transaction.html")

def transactions_page(request):
    return render(request, "transactions.html")

def categories_page(request):
    return render(request, "categories.html")

def create_category_page(request):
    return render(request, "create_category.html")

def profile_page(request):
    return render(request, "profile.html")
