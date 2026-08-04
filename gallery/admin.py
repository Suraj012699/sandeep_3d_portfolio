from django.contrib import admin

from .models import (
    ARProduct,
    AboutSection,
    BigImageSection,
    FeaturedDoubleSlider,
    Model3D,
    PortfolioVideo,
    Project,
    SliderSection,
)


class ProjectInline(admin.TabularInline):
    model = Project
    extra = 1

    fields = (
        "order",
        "title",
        "category",
        "image_path",
        "thumbnail",
        "software_used",
        "section",
        "featured_section",
        "model_file_link",
    )

    ordering = ("order",)


@admin.register(FeaturedDoubleSlider)
class FeaturedDoubleSliderAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "order",
    )

    list_editable = ("order",)
    ordering = ("order",)
    inlines = [ProjectInline]


@admin.register(SliderSection)
class SliderSectionAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "order",
    )

    list_editable = ("order",)
    ordering = ("order",)
    inlines = [ProjectInline]


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "section",
        "featured_section",
        "order",
        "has_permanent_image",
    )

    list_editable = ("order",)

    list_filter = (
        "section",
        "featured_section",
        "category",
    )

    search_fields = (
        "title",
        "category",
        "software_used",
        "image_path",
    )

    ordering = ("order",)

    fieldsets = (
        (
            "Project Information",
            {
                "fields": (
                    "title",
                    "category",
                    "software_used",
                    "order",
                )
            },
        ),
        (
            "Section Placement",
            {
                "fields": (
                    "section",
                    "featured_section",
                )
            },
        ),
        (
            "Permanent Project Image",
            {
                "fields": ("image_path",),
                "description": (
                    "Recommended: image ko static folder me rakhein aur "
                    "yahan uska path enter karein."
                ),
            },
        ),
        (
            "Old Uploaded Image Fallback",
            {
                "fields": ("thumbnail",),
                "classes": ("collapse",),
            },
        ),
        (
            "External Link",
            {
                "fields": ("model_file_link",),
            },
        ),
    )

    @admin.display(boolean=True, description="Permanent Image")
    def has_permanent_image(self, obj):
        return bool(obj.image_path)


@admin.register(Model3D)
class Model3DAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "category",
        "software_used",
        "created_at",
        "has_permanent_image",
    )

    search_fields = (
        "title",
        "category",
        "software_used",
        "image_path",
    )

    list_filter = ("category",)

    fieldsets = (
        (
            "Project Details",
            {
                "fields": (
                    "title",
                    "category",
                    "description",
                    "software_used",
                    "model_file_link",
                )
            },
        ),
        (
            "Permanent Files",
            {
                "fields": (
                    "image_path",
                    "video_path",
                )
            },
        ),
        (
            "Old Uploaded Files",
            {
                "fields": (
                    "thumbnail",
                    "video_snippet",
                ),
                "classes": ("collapse",),
            },
        ),
    )

    @admin.display(boolean=True, description="Permanent Image")
    def has_permanent_image(self, obj):
        return bool(obj.image_path)


@admin.register(PortfolioVideo)
class PortfolioVideoAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "created_at",
        "has_permanent_video",
    )

    search_fields = (
        "title",
        "video_path",
    )

    fields = (
        "title",
        "video_path",
        "video_file",
    )

    @admin.display(boolean=True, description="Permanent Video")
    def has_permanent_video(self, obj):
        return bool(obj.video_path)


@admin.register(BigImageSection)
class BigImageSectionAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "has_permanent_image",
    )

    fields = (
        "title",
        "image_path",
        "image",
        "ar_link",
    )

    @admin.display(boolean=True, description="Permanent Image")
    def has_permanent_image(self, obj):
        return bool(obj.image_path)


@admin.register(ARProduct)
class ARProductAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "order",
        "has_permanent_image",
    )

    list_editable = ("order",)
    ordering = ("order",)

    search_fields = (
        "title",
        "image_path",
    )

    fields = (
        "title",
        "order",
        "image_path",
        "image",
        "ar_link",
    )

    @admin.display(boolean=True, description="Permanent Image")
    def has_permanent_image(self, obj):
        return bool(obj.image_path)


@admin.register(AboutSection)
class AboutSectionAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "experience_years",
        "has_permanent_photo",
    )

    fields = (
        "experience_years",
        "photo_path",
        "photo",
    )

    @admin.display(boolean=True, description="Permanent Photo")
    def has_permanent_photo(self, obj):
        return bool(obj.photo_path)