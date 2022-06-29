# from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response

# possible GET, PUT, POST
@api_view(["GET"])
def getRoutes(request):
    routes = [
        "GET /api",
        "GET /api/rooms",
        "GET / api/rooms/:id",
    ]
    # Return Json with NOT only "dict" objects - JsonResponse
    return Response(routes)
