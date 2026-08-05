from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from gallery import views


admin.site.site_header = "Sandeep Portfolio Administration"
admin.site.site_title = "Sandeep Admin"
admin.site.index_title = "Portfolio Content Management"


urlpatterns = [
    path(
        "admin/",
        admin.site.urls,
    ),

    path(
        "",
        views.home,
        name="home",
    ),

    path(
        "about/",
        views.views_about,
        name="about",
    ),

    path(
        "contact/",
        views.views_contact,
        name="contact",
    ),
]


# Uploaded media ko sirf local development me Django serve karega.
if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT,
    )