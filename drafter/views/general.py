from django.shortcuts import render


def index(request):
    return render(request, 'drafter/index.html')
#

# from django.shortcuts import render
#
#
# def index(request):
#     return render(request, 'drafter/angular/index.html')