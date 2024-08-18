from rest_framework import serializers
from django.contrib.auth.models import User
from exam_question.models import ExamQuestion

class ExamQuestionSerializer(serializers.ModelSerializer):
    last_modified_by = serializers.ReadOnlyField(source="last_modified_by.username")

    class Meta:
        model = ExamQuestion
        fields = ["id", "subject", "question_content", "question_choices", "answer", "mark", "mix_choices", "created_at", "modified_at", "last_modified_by"]

class UserSerializer(serializers.ModelSerializer):
    exam_questions = serializers.PrimaryKeyRelatedField(many=True, queryset=ExamQuestion.objects.all())

    class Meta:
        model = User
        fields = ["id", "username", "exam_questions"]