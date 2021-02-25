from django.urls import path, include
from .views import article_list, article_detail, ArticleClass, DetailClass, ArticleMixinClass, DetailMixinClass, ArticleViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('article', ArticleViewSet, basename='artice')

urlpatterns = [
    path('viewset/', include(router.urls)),
    path('article/', article_list),
    path('articleclass/', ArticleClass.as_view()),
    path('articlemixin', ArticleMixinClass.as_view()),
    path('detail/<int:pk>/', article_detail),
    path('detailclass/<int:pk>/', DetailClass.as_view()),
    path('detailmixin/<int:pk>/', DetailMixinClass.as_view()),
]
