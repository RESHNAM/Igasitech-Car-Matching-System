from django.db import models
from django.utils.translation import gettext_lazy as _
from car_matching.settings.base import AUTH_USER_MODEL
from apps.common.models import TimeStampedUUIDModel
from apps.profiles.models import Profile

# Create your models here.
class Rating(TimeStampedUUIDModel):

    class Range(models.IntegerChoices):
        RATING_1 = 1, _("Poor")
        RATING_2 = 2, _("Fair")
        RATING_3 = 3, _("Good")
        RATING_4 = 4, _("Very Good")
        RATING_5 = 5, _("Excellent")

    rater = models.ForeignKey(AUTH_USER_MODEL, verbose_name=_("User providing the rating"), on_delete=models.SET_NULL, null=True)
    seller = models.ForeignKey(Profile, verbose_name=_("Seller being rated"), related_name="seller_review", on_delete=models.SET_NULL, null=True)
    rating = models.IntegerField(verbose_name=_("Rating"), choices=Range.choices, help_text="1=Poor, 2=Fair, 3=Good, 4=Very good, 5=Excellent", default=0)
    comment = models.TextField(verbose_name=_("Comment"))

    class Meta:
        unique_together = ["rater","seller"]

    def __str__(self):
        return f"{self.seller} rated at {self.rating}"


