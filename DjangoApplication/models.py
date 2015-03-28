from django.db import models
from django.contrib.auth.models import User

# Implementation parameters.
# (At the moment there are none.)

# Various size-limited character fields. Consistency is useful.
class CharAbbr (models.CharField):
    """Abbreviated names: very short."""
    def __init__ (self, *args, **kwargs):
        super (CharAbbr, self).__init__ (max_length=4,
                                         *args, **kwargs)
class CharName (models.CharField):
    """Full names: long enough to be unique and mnemonic."""
    def __init__ (self, *args, **kwargs):
        super (CharName, self).__init__ (max_length=20,
                                         *args, **kwargs)
class CharNote (models.CharField):
    """Verbose text: optional descriptive prose."""
    def __init__ (self, null=True, *args, **kwargs):
        super (CharNote, self).__init__ (max_length=1200,
                                         null=null,
                                         *args, **kwargs)

# We subclass User to turn it into something more flexible someday.
class JobOwner (User):
    """This will include some more elaborate permission mechanism."""
    pass

# All models have a default ID field.

class JobState (models.Model):
    """The state of a Job, e.g., finished, in process, whatever."""
    abbrev = CharAbbr ()
    name = CharName ()
    desc = CharNote ()

class Job (models.Model):
    """An individual task to be scheduled. Grist for the mill."""
    name = CharName ()
    desc = CharNote ()
    owner = models.ForeignKey (JobOwner, null=True)
    state = models.ForeignKey (JobState)

class JobEventType (models.Model):
    """A classification of events in the Log."""
    abbrev = CharAbbr ()
    name = CharName ()
    desc = CharNote ()

class JobLog (models.Model):
    """A state change for a Job."""
    job = models.ForeignKey (Job)
    owner = models.ForeignKey (JobOwner, null=True)
    event = models.ForeignKey (JobEventType)
    timestamp = models.DateTimeField (auto_now_add=True)
    note = CharNote ()
