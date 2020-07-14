from django.urls import path

from .views import DataListView, DataDetailView

urlpatterns = [
    path('', DataListView.as_view()),
    path('<pk>', DataDetailView.as_view())
]
