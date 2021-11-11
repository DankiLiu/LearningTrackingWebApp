from django.db import models
from django.contrib.auth.models import User


class Project(models.Model):
    """A learning plan of a user."""
    project_name = models.CharField(max_length=50)
    project_description = models.CharField(max_length=200)
    start_date = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User,
                              on_delete=models.CASCADE)

    def __str__(self):
        """Return a string representation of the model."""
        return self.project_name


class Entry(models.Model):
    """Something specific about a LearningProject. eg. material"""
    project = models.ForeignKey(Project,
                                on_delete=models.CASCADE)
    entry_name = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        """Returning a string representation of the model."""
        return "Material: " + self.entry_name[:50]