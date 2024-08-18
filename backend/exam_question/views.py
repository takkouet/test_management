from exam_question.models import ExamQuestion
from exam_question.serializers import ExamQuestionSerializer
from exam_question.serializers import UserSerializer
from rest_framework import generics
from rest_framework import permissions
from django.contrib.auth.models import User

class ExamQuestionList(generics.ListAPIView):
    queryset = ExamQuestion.objects.all()
    serializer_class = ExamQuestionSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(last_modified_by=self.request.user)

class ExamQuestionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ExamQuestion.objects.all()
    serializer_class = ExamQuestionSerializer

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
