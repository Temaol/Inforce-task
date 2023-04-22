from django.db import models

from restaurant.models import Restaurant


class Menu(models.Model):
    """Model representing a restaurant menu"""
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    title = models.CharField(max_length=255, blank=False, null=False)
    components = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-created_at',)

    def __str__(self):
        return f"{self.title} ({self.restaurant.title})"
