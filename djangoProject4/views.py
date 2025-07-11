from django.shortcuts import render

def main(request):
    return render(request, template_name='main.html')

def about(request):
    return render(request, template_name='about.html')