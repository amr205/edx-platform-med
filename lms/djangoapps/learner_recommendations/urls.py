"""
Learner Recommendations URL routing configuration.
"""

from django.conf import settings
from django.urls import re_path

from lms.djangoapps.learner_recommendations import views

app_name = "learner_recommendations"

urlpatterns = [
    re_path(fr'^amplitude/{settings.COURSE_ID_PATTERN}/$',
            views.AboutPageRecommendationsView.as_view(),
            name='amplitude_recommendations'),
    re_path(r"^courses/$",
            views.HomeRecommendationsApiView.as_view(),
            name="courses"),
]
