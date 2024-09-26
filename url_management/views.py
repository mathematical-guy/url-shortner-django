from django.shortcuts import render, redirect
from .models import ShortenedURL
from django.views.generic.detail import DetailView


class RedirectToLargeURLView(DetailView):
    queryset = ShortenedURL.objects.all()

    def get(self, request, *args, **kwargs):
        url_object: ShortenedURL = self.get_object(queryset=self.queryset)
        return redirect(to=url_object.original_url)
