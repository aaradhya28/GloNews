from django.shortcuts import render,redirect
import os
import requests
from dotenv import load_dotenv
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics
from pathlib import Path
from .models import News
from .serializers import NewsSerializer
from datetime import datetime
from .models import Visitor


BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv(BASE_DIR / ".env")

API_KEY = os.getenv("NEWS_API_KEY")

print("API KEY:", API_KEY)

def home(request):
    return render(request, 'home.html')

class LiveNewsView(APIView):
    def get(self, request):
        query = request.GET.get('q')
        country = request.GET.get('country', 'in')
        category = request.GET.get('category', None)

        if query:
            url = "https://newsapi.org/v2/everything"
            params = {
                "apiKey": API_KEY,
                "q": query,
                "language": "en",
                "sortBy": "publishedAt",
                "pageSize": 10
            }
        else:
            url = "https://newsapi.org/v2/top-headlines"
            params = {
                "apiKey": API_KEY,
                "country": country,
                "pageSize": 10
            }

            if category:
                params["category"] = category

        response = requests.get(url, params=params)
        data = response.json()

        # fallback for India
        if data.get("totalResults") == 0:
            params["country"] = "us"
            response = requests.get(url, params=params)
            data = response.json()

        return Response(data)
    
def entry_page(request):
    if request.method == "POST":
        name = request.POST.get("name")

        if name:
            Visitor.objects.create(name=name)
            return redirect("/home/")  
    return render(request, "entry.html")

    

# List all news
class NewsListView(generics.ListAPIView):
    queryset = News.objects.all().order_by('-published_at')
    serializer_class = NewsSerializer

# Get single news
class NewsDetailView(generics.RetrieveAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer

# Filter by category
class NewsByCategoryView(generics.ListAPIView):
    serializer_class = NewsSerializer

    def get_queryset(self):
        category = self.kwargs['category']
        return News.objects.filter(category__iexact=category)