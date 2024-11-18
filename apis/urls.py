from django.urls import path

from apis.views import GreekViews

urlpatterns = [
    path('view/', GreekViews.as_view(), name= "view"),
]