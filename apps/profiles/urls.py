from django.urls import path

from .views import *

urlpatterns = [
    path("me/", GetProfileAPIView.as_view(), name="get_profile"),
    path("update/<str:username>/", UpdateProfileAPIView.as_view(), name="update_profile"),
    path("sellers/all/", SellerListAPIView.as_view(), name="all_sellers"),
    path("buyers/all/", BuyerListAPIView.as_view(), name="all_buyers"),
]