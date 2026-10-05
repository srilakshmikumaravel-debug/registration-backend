from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Registration
import json


@csrf_exempt
def register(request):

    if request.method == "POST":

        data = json.loads(request.body)

        name = data.get("name")
        email = data.get("email")
        password = data.get("password")

        Registration.objects.create(
            name=name,
            email=email,
            password=password
        )

        return JsonResponse({
            "message": "Registration successful"
        })

    return JsonResponse({
        "message": "Only POST method is allowed"
    })