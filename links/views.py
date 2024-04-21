from django.views.generic.list import ListView

from .models import Link


class LinkListView(ListView):
    model = Link
