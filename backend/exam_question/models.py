from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User
import json

# Create your models here.
class ExamQuestion(models.Model):
    id = models.AutoField(primary_key=True)
    subject = models.CharField(max_length=100, blank=True)
    question_content = models.CharField(max_length=200, null=False, unique=True)
    question_choices = models.TextField(max_length=500, null=False)
    answer = models.CharField(max_length=100, null=False)
    mark = models.DecimalField(validators=[MinValueValidator(0), MaxValueValidator(10)], null=False, max_digits=2, decimal_places=1)
    unit = models.CharField(max_length=20)
    mix_choices = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    last_modified_by = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name="exam_questions")

    def set_question_choices(self, question_choices):
        self.question_choices = json.dumps(question_choices)

    def get_question_choices(self):
        return json.loads(self.question_choices)

    def __str__(self) -> str:
        return self.question_content