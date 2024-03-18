# main/views.py

from django.http import JsonResponse
from .models import MainContent, MenuItem, Logo, Feature

def main_page_content(request):
    
    items = MenuItem.objects.all().values('name', 'url', 'order').order_by('order')
    logo = Logo.objects.filter(active=True).first()  
    logo_url = logo.image.url if logo else None  
    content = MainContent.objects.first()
    background_url = content.background_image.url if content and content.background_image else None
    button_text = content.button_text if content else None
    title_text = content.title_text if content else None 

    return JsonResponse({
        'menu_items': list(items),
        'logo_url': logo_url,
        'background_url': background_url,
        'button_text': button_text,
        'title_text': title_text,
    })
    
def features_content(request):
    features = Feature.objects.all().values('title', 'value', 'description')
    return JsonResponse({'features': list(features)})