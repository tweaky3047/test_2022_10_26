from django.shortcuts import render
from rest_framework.decorators import api_view
from articles.models import Article
from articles.serializers import Article, ArticleSerializer
from rest_framework.response import Response
# Create your views here.

@api_view(['GET','POST'])
def index(request):
    articles = Article.objects.all()  
    serializers = ArticleSerializer(articles, many=True)
    return Response(serializers.data)