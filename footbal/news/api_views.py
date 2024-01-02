from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from news.models import News, Category
from news.serializer import NewsSerializer, CategorySerializer


class AllNewsAPI(generics.ListAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    permission_classes = (IsAuthenticated, )


class AllCategoryAPI(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (IsAuthenticated, )


class NewsByCategory(generics.ListAPIView):
    serializer_class = NewsSerializer
    permission_classes = (IsAuthenticated, )

    def get_queryset(self):
        return News.objects.filter(category__pk=self.kwargs['cat_pk']).order_by('-created_at')


class CreateNewsAPI(generics.CreateAPIView):
    serializer_class = NewsSerializer
    queryset = News.objects.all()
    permission_classes = (IsAuthenticated, )


class GetUpdateDeleteNewsAPI(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = NewsSerializer
    permission_classes = (IsAuthenticated, )
    queryset = News.objects.all()

