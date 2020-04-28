from django.shortcuts import render


def homepage(request):
    return render(request, 'homepage.html', {})


def ecommerce_report_page(request):
    return render(request, 'marketing_report.html', {})


def marketing_report_page(request):
    return render(request, 'marketing_report.html', {})
