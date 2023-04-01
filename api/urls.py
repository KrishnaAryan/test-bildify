
from django.urls import path
from api.views import ProjectCreateAPIView

urlpatterns = [
    path('projects/', ProjectCreateAPIView.as_view(), name='project'),
]
