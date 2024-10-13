from rest_framework import serializers
from .models import Rating


class RatingSerializer(serializers.ModelSerializer):

    rater = serializers.SerializerMethodField(read_only=True)
    seller = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Rating
        exclude = ["updated_at", "pkid"]

    def get_rater(self, obj):
        return obj.rater.username
    
    def get_seller(self, obj):
        return obj.seller.user.username
