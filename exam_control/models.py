from django.db import models

from account_control.models import UserModel
from common.choices import ExamType
from common.models import BaseModel


class ExamModel(BaseModel):
    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    total_duration = models.IntegerField(default=0)
    student_duration = models.IntegerField(default=0)
    total_score = models.FloatField(default=0)
    is_published = models.BooleanField(default=False)
    is_completed = models.BooleanField(default=False)

    class Meta:
        db_table = 'exam'
        verbose_name = 'Exam'
        verbose_name_plural = 'Exams'
        ordering = ['-created_at']

    def __str__(self):
        return self.title


class QuestionModel(BaseModel):
    exam = models.ForeignKey(ExamModel, on_delete=models.RESTRICT, related_name='questions')
    type = models.CharField(max_length=4, choices=ExamType.choices, default=ExamType.MCQ)
    prompt = models.TextField(null=True, blank=True)

    class Meta:
        db_table = 'question'
        verbose_name = 'Question'
        verbose_name_plural = 'Questions'
        ordering = ['id']

    def __str__(self):
        return self.prompt


class QuestionAttachmentModel(BaseModel):
    question = models.ForeignKey(QuestionModel, on_delete=models.RESTRICT, related_name='attachments')
    attachment = models.FileField(upload_to='question_attachments/')

    class Meta:
        db_table = 'question_attachment'
        verbose_name = 'Question Attachment'
        verbose_name_plural = 'Question Attachments'
        ordering = ['id']

    def __str__(self):
        return self.attachment.name


class OptionModel(BaseModel):
    question = models.ForeignKey(QuestionModel, on_delete=models.RESTRICT, related_name='options')
    text = models.TextField(null=True, blank=True)
    is_correct = models.BooleanField(default=False)

    class Meta:
        db_table = 'option'
        verbose_name = 'Option'
        verbose_name_plural = 'Options'
        ordering = ['id']


class OptionAttachmentModel(BaseModel):
    option = models.ForeignKey(OptionModel, on_delete=models.RESTRICT, related_name='attachments')
    attachment = models.FileField(upload_to='option_attachments/')

    class Meta:
        db_table = 'option_attachment'
        verbose_name = 'Option Attachment'
        verbose_name_plural = 'Option Attachments'
        ordering = ['id']


class ExamAssignmentModel(BaseModel):
    exam = models.ForeignKey(ExamModel, on_delete=models.RESTRICT, related_name='assignments')
    students = models.ManyToManyField(UserModel, related_name='exam_assignments')

    class Meta:
        db_table = 'exam_assignment'
        verbose_name = 'Exam Assignment'
        verbose_name_plural = 'Exam Assignments'
        ordering = ['id']

    def __str__(self):
        return f'{self.exam.title} - {self.created_at}'


class StudentSubmissionModel(BaseModel):
    exam = models.ForeignKey(ExamModel, on_delete=models.RESTRICT, related_name='submissions')
    student = models.ForeignKey(UserModel, on_delete=models.RESTRICT, related_name='exam_submissions')
    started_at = models.DateTimeField(null=True, blank=True)
    submitted_at = models.DateTimeField(null=True, blank=True)
    duration = models.IntegerField(default=0)
    score = models.IntegerField(default=0)
    is_graded = models.BooleanField(default=False)
    feedback = models.TextField(null=True, blank=True)

    class Meta:
        db_table = 'student_submission'
        verbose_name = 'Student Submission'
        verbose_name_plural = 'Student Submissions'
        ordering = ['-created_at']


class StudentSubmissionAnswerModel(BaseModel):
    submission = models.ForeignKey(StudentSubmissionModel, on_delete=models.RESTRICT, related_name='answers')
    question = models.ForeignKey(QuestionModel, on_delete=models.RESTRICT, related_name='answers')
    option = models.ForeignKey(OptionModel, on_delete=models.RESTRICT, related_name='answers', null=True, blank=True)
    text = models.TextField(null=True, blank=True)
    is_correct = models.BooleanField(default=False)
    score = models.IntegerField(default=0)
    feedback = models.TextField(null=True, blank=True)

    class Meta:
        db_table = 'student_submission_answer'
        verbose_name = 'Student Submission Answer'
        verbose_name_plural = 'Student Submission Answers'
        ordering = ['-created_at']
