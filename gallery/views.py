from django.contrib.auth.models import User
from django.shortcuts import render
from .models import Model3D,ARProduct, BigImageSection, PortfolioVideo, SliderSection, FeaturedDoubleSlider

def home(request):
    if not User.objects.filter(username='sandeep_admin').exists():
        User.objects.create_superuser('sandeep_admin', 'admin@example.com', 'Sandeep@123')
    slider_sections = SliderSection.objects.prefetch_related('projects').all().order_by('order')
    featured_doubles = FeaturedDoubleSlider.objects.prefetch_related('featured_items').all().order_by('order')
    
    projects = Model3D.objects.all().order_by('-created_at')[:2]
    portfolio_videos = PortfolioVideo.objects.all() 
    big_image_data = BigImageSection.objects.last()
    ar_products = ARProduct.objects.all().order_by('order')
    
    context = {
        'projects': projects,
        'slider_sections': slider_sections,
        'big_image_data': big_image_data,
        'featured_doubles': featured_doubles,
        'ar_products': ar_products,
        'portfolio_videos': portfolio_videos,
    }
    
    return render(request, 'gallery/index.html', context)

def views_about(request):
    return render(request, 'gallery/about.html')

def views_contact(request):
    return render(request, 'gallery/contact.html')