from django.shortcuts import render
from django.http import JsonResponse
from django.views import View

# Create your views here.

class FirstView(View):
    def get(self, request):
        return JsonResponse({"hello", "world", "method": request.method})
    def post(self, request):
        return JsonResponse({"hello", "world", "method": request.method})
    def put(self, request):
        return JsonResponse({"hello", "world", "method": request.method})
    def delete(self, request):
        return JsonResponse({"hello", "world", "method": request.method})