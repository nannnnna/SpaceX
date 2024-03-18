from django.urls import path
from . import views
from .views import features_content


urlpatterns = [
    path('api/main-page-content/', views.main_page_content, name='main-page-content'),
    path('api/features-content/', features_content, name='features-content'),
]
