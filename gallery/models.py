from django.db import models
from django.templatetags.static import static


def get_static_or_uploaded_url(static_path, uploaded_file):
    """
    Pehle project ke static folder ka path use karega.
    Agar static path nahi diya hai, to purani uploaded file use karega.
    """
    if static_path:
        return static(static_path)

    if uploaded_file:
        try:
            return uploaded_file.url
        except (ValueError, AttributeError):
            return ""

    return ""


class SliderSection(models.Model):
    name = models.CharField(max_length=200)
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ["order"]

    def __str__(self):
        return self.name


class FeaturedDoubleSlider(models.Model):
    name = models.CharField(
        max_length=200,
        help_text="Example: Featured Showcase",
    )
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ["order"]

    def __str__(self):
        return self.name


class Model3D(models.Model):
    title = models.CharField(max_length=200)
    category = models.CharField(max_length=100)

    description = models.TextField(
        blank=True,
        null=True,
    )

    # Purani uploaded image ke support ke liye rakha gaya hai.
    thumbnail = models.ImageField(
        upload_to="thumbnails/",
        blank=True,
        null=True,
    )

    # Nayi permanent static image ke liye.
    image_path = models.CharField(
        max_length=500,
        blank=True,
        help_text=(
            "Permanent image path. Example: "
            "gallery/assets/images/product-design-01.jpg"
        ),
    )

    video_snippet = models.FileField(
        upload_to="videos/",
        blank=True,
        null=True,
        help_text="Optional uploaded hover video.",
    )

    video_path = models.CharField(
        max_length=500,
        blank=True,
        help_text=(
            "Permanent video path. Example: "
            "gallery/assets/videos/product-animation.mp4"
        ),
    )

    software_used = models.CharField(
        max_length=200,
        blank=True,
        null=True,
    )

    model_file_link = models.URLField(
        blank=True,
        help_text="Sketchfab, Google Drive ya kisi external model ka link.",
    )

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    @property
    def image_url(self):
        return get_static_or_uploaded_url(
            self.image_path,
            self.thumbnail,
        )

    @property
    def video_url(self):
        return get_static_or_uploaded_url(
            self.video_path,
            self.video_snippet,
        )

    def __str__(self):
        return self.title


class Project(models.Model):
    section = models.ForeignKey(
        SliderSection,
        related_name="projects",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )

    featured_section = models.ForeignKey(
        FeaturedDoubleSlider,
        related_name="featured_items",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )

    title = models.CharField(max_length=200)
    category = models.CharField(max_length=100)

    software_used = models.CharField(
        max_length=100,
        blank=True,
        null=True,
    )

    # Purani uploaded image ke support ke liye.
    thumbnail = models.ImageField(
        upload_to="projects/thumbnails/",
        blank=True,
        null=True,
    )

    # Nayi permanent image ke liye.
    image_path = models.CharField(
        max_length=500,
        blank=True,
        help_text=(
            "Permanent image path. Example: "
            "gallery/assets/images/airstream-front.jpg"
        ),
    )

    model_file_link = models.URLField(blank=True)

    order = models.IntegerField(
        default=0,
        help_text="0, 1, 2, 3... ke through display order set karein.",
    )

    class Meta:
        ordering = ["order"]

    @property
    def image_url(self):
        return get_static_or_uploaded_url(
            self.image_path,
            self.thumbnail,
        )

    def __str__(self):
        section_name = "Unassigned"

        if self.section:
            section_name = self.section.name
        elif self.featured_section:
            section_name = self.featured_section.name

        return f"{section_name} - {self.title}"


class PortfolioVideo(models.Model):
    title = models.CharField(max_length=200)

    # Purane uploaded video ke support ke liye.
    video_file = models.FileField(
        upload_to="projects/videos/",
        blank=True,
        null=True,
    )

    # Naye permanent video ke liye.
    video_path = models.CharField(
        max_length=500,
        blank=True,
        help_text=(
            "Permanent video path. Example: "
            "gallery/assets/videos/walk-through.mp4"
        ),
    )

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["created_at"]

    @property
    def video_url(self):
        return get_static_or_uploaded_url(
            self.video_path,
            self.video_file,
        )

    def __str__(self):
        return self.title


class BigImageSection(models.Model):
    title = models.CharField(
        max_length=200,
        default="AR Experience",
    )

    # Purani uploaded image.
    image = models.ImageField(
        upload_to="big_images/",
        blank=True,
        null=True,
    )

    # Nayi permanent image.
    image_path = models.CharField(
        max_length=500,
        blank=True,
        help_text=(
            "Permanent image path. Example: "
            "gallery/assets/images/ar-view-main.jpg"
        ),
    )

    ar_link = models.URLField(
        max_length=500,
        blank=True,
        null=True,
    )

    @property
    def image_url(self):
        return get_static_or_uploaded_url(
            self.image_path,
            self.image,
        )

    def __str__(self):
        return self.title


class ARProduct(models.Model):
    title = models.CharField(
        max_length=200,
        blank=True,
        null=True,
    )

    # Purani uploaded image.
    image = models.ImageField(
        upload_to="ar_products/",
        blank=True,
        null=True,
    )

    # Nayi permanent image.
    image_path = models.CharField(
        max_length=500,
        blank=True,
        help_text=(
            "Permanent image path. Example: "
            "gallery/assets/images/ar-product-01.jpg"
        ),
    )

    ar_link = models.URLField(
        max_length=500,
        blank=True,
    )

    order = models.IntegerField(default=0)

    class Meta:
        ordering = ["order"]

    @property
    def image_url(self):
        return get_static_or_uploaded_url(
            self.image_path,
            self.image,
        )

    def __str__(self):
        return self.title or f"AR Product {self.pk}"


class AboutSection(models.Model):
    # Purani uploaded photo.
    photo = models.ImageField(
        upload_to="about_photos/",
        blank=True,
        null=True,
    )

    # Nayi permanent photo.
    photo_path = models.CharField(
        max_length=500,
        blank=True,
        help_text=(
            "Permanent photo path. Example: "
            "gallery/assets/images/sandeep-profile.jpg"
        ),
    )

    experience_years = models.DecimalField(
        max_digits=4,
        decimal_places=1,
        default=8.5,
    )

    @property
    def photo_url(self):
        return get_static_or_uploaded_url(
            self.photo_path,
            self.photo,
        )

    def __str__(self):
        return "About Section Content"