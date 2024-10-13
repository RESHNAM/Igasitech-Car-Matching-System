from django.contrib import admin
from .models import Rating

# Register your models here.
class RatingAdmin(admin.ModelAdmin):
    list_display = ["rater", "seller", "rating"]


admin.site.register(Rating, RatingAdmin)
