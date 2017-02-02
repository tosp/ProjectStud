from django.shortcuts import render


def home_directory(request):
    return render(request, "spaced_repetition/home_directory.html")
