from django.contrib import admin
from django.urls import path

from url_management.views import RedirectToLargeURLView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('<str:pk>/', RedirectToLargeURLView.as_view()),
]
