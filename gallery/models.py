from django.db import models

class SliderSection(models.Model):
    name = models.CharField(max_length=200)
    order = models.IntegerField(default=0)

    def __str__(self):
        return self.name

class FeaturedDoubleSlider(models.Model):
    name = models.CharField(max_length=200, help_text="e.g. Featured Showcase 1")
    order = models.IntegerField(default=0)

    def __str__(self):
        return self.name

class Model3D(models.Model):
    title = models.CharField(max_length=200)
    category = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    thumbnail = models.ImageField(upload_to='thumbnails/')
    video_snippet = models.FileField(upload_to='videos/', blank=True, null=True, help_text="Hover effect ke liye chota .mp4 video upload karein.")
    software_used = models.CharField(max_length=200, blank=True, null=True)
    model_file_link = models.URLField(blank=True, help_text="Sketchfab ya Google Drive ka link")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Project(models.Model):
    section = models.ForeignKey(SliderSection, related_name='projects', on_delete=models.CASCADE, null=True, blank=True)
    featured_section = models.ForeignKey(FeaturedDoubleSlider, related_name='featured_items', on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=200)
    category = models.CharField(max_length=100)
    software_used = models.CharField(max_length=100, blank=True, null=True)
    thumbnail = models.ImageField(upload_to='projects/thumbnails/')
    model_file_link = models.URLField(blank=True)
    order = models.IntegerField(default=0, help_text="Yahan number daliye (0, 1, 2...) order set karne ke liye")

    class Meta:
        ordering = ['order']

    def __str__(self):
        s_name = self.section.name if self.section else (self.featured_section.name if self.featured_section else "Unassigned")
        return f"{s_name} - {self.title}"

class PortfolioVideo(models.Model):
    title = models.CharField(max_length=200)
    video_file = models.FileField(upload_to='projects/videos/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class BigImageSection(models.Model):
    title = models.CharField(max_length=200, default="AR Experience")
    image = models.ImageField(upload_to='big_images/')
    ar_link = models.URLField(max_length=500, blank=True, null=True)
    def __str__(self): 
        return self.title
    
class ARProduct(models.Model):
    title = models.CharField(max_length=200,blank=True,null=True)
    image = models.ImageField(upload_to='ar_products/')
    ar_link = models.URLField(max_length=500)
    order = models.IntegerField(default=0)
    def __str__(self): 
        return self.title

class AboutSection(models.Model):
    photo = models.ImageField(upload_to='about_photos/')
    experience_years = models.DecimalField(max_digits=4, decimal_places=1, default=8.5)
    
    def __str__(self):
        return "About Section Content"