from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.views import generic

from JobJarApplication.models import *

class IndexView (generic.ListView):
    """Home page: list of interesting jobs."""
    template_name = "JobJar/index.html"
    context_object_name = "jobs"

    def get_queryset (self):
        """Return active jobs."""
        active = [JOB_STATES_ABBR[x]
                  for x in ('new', 'busy', 'wait', 'what')]
        return Job.objects.filter (state__in=active)
