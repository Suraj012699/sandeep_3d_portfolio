from django.contrib import admin
from .models import Model3D,ARProduct,AboutSection, FeaturedDoubleSlider, BigImageSection, PortfolioVideo, SliderSection, Project

class ProjectInline(admin.TabularInline):
    model = Project
    extra = 1
    fields = ('order', 'title', 'category', 'thumbnail', 'software_used', 'section', 'featured_section', 'model_file_link')
    ordering = ('order',)

@admin.register(FeaturedDoubleSlider)
class FeaturedDoubleSliderAdmin(admin.ModelAdmin):
    list_display = ('name', 'order')
    list_editable = ('order',)
    inlines = [ProjectInline]

@admin.register(SliderSection)
class SliderSectionAdmin(admin.ModelAdmin):
    list_display = ('name', 'order')
    list_editable = ('order',)
    inlines = [ProjectInline]

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'section', 'featured_section', 'order')
    list_editable = ('order',)
    list_filter = ('section', 'featured_section')

@admin.register(Model3D)
class Model3DAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'software_used', 'created_at')

@admin.register(PortfolioVideo)
class PortfolioVideoAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')

@admin.register(BigImageSection)
class BigImageSectionAdmin(admin.ModelAdmin):
    list_display = ('title',)

@admin.register(ARProduct)
class ARProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'order')
    list_editable = ('order',)

@admin.register(AboutSection)
class AboutSectionAdmin(admin.ModelAdmin):
    list_display = ('id', 'experience_years')