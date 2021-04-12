from django.urls import path
from .views import indexview,aboutview

urlpatterns = [
    path('', indexview.as_view()),
    path('about/',aboutview.as_view())
]
