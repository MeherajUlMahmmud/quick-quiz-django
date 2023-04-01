from django.urls import path, include
from rest_framework.routers import DefaultRouter

from exam_control.views.exam import ExamModelViewSet
from exam_control.views.option import OptionModelViewSet, OptionAttachmentModelViewSet
from exam_control.views.question import QuestionModelViewSet, QuestionAttachmentModelViewSet
from exam_control.views.submission import StudentSubmissionViewSet, StudentSubmissionAnswerModelViewSet

router = DefaultRouter()
router.register(r'exam', ExamModelViewSet, basename='exam')
router.register(r'question', QuestionModelViewSet, basename='question')
router.register(r'question-attachment', QuestionAttachmentModelViewSet, basename='question_attachment')
router.register(r'option', OptionModelViewSet, basename='option')
router.register(r'option-attachment', OptionAttachmentModelViewSet, basename='option_attachment')
router.register(r'submission', StudentSubmissionViewSet, basename='submission')
router.register(r'submission-answer', StudentSubmissionAnswerModelViewSet, basename='submission_answer')

urlpatterns = [
    path('', include(router.urls)),
]
