from django.db import models

# Implementation parameters.
CHAR_LIMITS = {
    'abbr' : 4,
    'name' : 20,
    'desc' : 120,
}

# Create your models here.

# All models have a default ID field.

class JobState (models.Model):
    """The state of a Job, e.g., finished, in process, whatever."""
    abbrev = models.CharField (max_length=CHAR_LIMITS['abbr'])
    name = models.CharField (max_length=CHAR_LIMITS['name'])
    desc = models.CharField (max_length=CHAR_LIMITS['desc'])

class Job (models.Model):
    """An individual task to be scheduled. Grist for the mill."""
    name = models.CharField (max_length=CHAR_LIMITS['name'])
    desc = models.CharField (max_length=CHAR_LIMITS['desc'])
    state = models.ForeignKey (JobState)

class JobEventType (models.Model):
    """A classification of events in the Log."""
    abbrev = models.CharField (max_length=CHAR_LIMITS['abbr'])
    name = models.CharField (max_length=CHAR_LIMITS['name'])
    desc = models.CharField (max_length=CHAR_LIMITS['desc'])

class JobLog (models.Model):
    """A state change for a Job."""
    job = models.ForeignKey (Job)
    event = models.ForeignKey (JobEventType)
    timestamp = models.DateTimeField (auto_now_add=True)
    note = models.CharField (max_length=CHAR_LIMITS['desc'])
