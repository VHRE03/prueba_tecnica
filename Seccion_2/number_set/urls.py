from django.urls import path
from .views import ExtractNumberView

urlpatterns = [
    path('extract/', ExtractNumberView.as_view(), name = 'extract-number')
]
