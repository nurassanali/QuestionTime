from django.urls import include, path
from questions.api import views as qv
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r"questions", qv.QuestionViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("questions/<slug:slug>/answer/", qv.AnswerCreateAPIView .as_view(), name="create-answer"),
    path("questions/<slug:slug>/answers/", qv.AnswerListAPIView.as_view(), name="list-answer"),
    path("answers/<int:pk>/", qv.AnswerRUDAPIView.as_view(), name="detail-answer"),
    path("answers/<int:pk>/like/", qv.AnswerLikeAPIView.as_view(), name="like-answer"),
]
