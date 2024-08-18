from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from exam_question import views

urlpatterns = [
    path("exam_questions/", views.ExamQuestionList.as_view()),
    path("exam_questions/<int:pk>/", views.ExamQuestionDetail.as_view()),
    path("users/", views.UserList.as_view()),
    path("users/<int:pk>/", views.UserDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)