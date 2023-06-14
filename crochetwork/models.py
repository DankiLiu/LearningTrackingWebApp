from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    """A learning plan of a user."""
    category_name = models.CharField(max_length=50)
    category_description = models.CharField(max_length=200)
    start_date = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User,
                              on_delete=models.CASCADE)

    def __str__(self):
        """Return a string representation of the model."""
        return self.category_name


class Entry(models.Model):
    """A handmade crocheting work"""
    category = models.ForeignKey(Category,
                                 null=True,
                                 on_delete=models.CASCADE)
    entry_name = models.TextField()
    entry_image = models.ImageField(upload_to='images/', default=None)
    # entry type [flowers, figures, ...]
    # entry with_templates, is upload with template, has a template instance as foreignkey
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        """Returning a string representation of the model."""
        return "My Work: " + self.entry_name[:50]
