from django.shortcuts import render

# Create your views here.

def test():
    return render("sample_app/test.html")