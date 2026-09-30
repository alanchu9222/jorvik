from django.http import JsonResponse

def health(request):
    return JsonResponse({
        "status": "healthy",
        "service": "jorvik-api"
    })

# Create your views here.
