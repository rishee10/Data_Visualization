from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import DataPoint
from django.core.serializers import serialize

@csrf_exempt
def get_data(request):
    queryset = DataPoint.objects.all()

    # Apply filters from request parameters
    filters = {
        'end_year': request.GET.get('end_year'),
        'topic': request.GET.get('topic'),
        'sector': request.GET.get('sector'),
        'region': request.GET.get('region'),
        'pestle': request.GET.get('pestle'),
        'source': request.GET.get('source'),
        'country': request.GET.get('country'),
        'city': request.GET.get('city'),
    }

    for field, value in filters.items():
        if value:
            queryset = queryset.filter(**{field + "__icontains": value})

    data = serialize('json', queryset)
    return JsonResponse({'data': data}, safe=False)

def dashboard(request):
    return render(request, 'index.html')

def visualization_page(request):
    return render(request, 'index2.html')
