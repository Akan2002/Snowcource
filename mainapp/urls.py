from django.urls import path

from rest_framework.routers import DefaultRouter as DR

from mainapp.views import (
    CategoryView, CourseScheduleView, CourseView, LearningTechnologyView, ClientView, RegistrationView, AuthorizationView, CommentView, PublicationView
)

router=DR()

router.register('category', CategoryView, basename='categories')
router.register('courseschedule', CourseScheduleView, basename='courseschedules')
router.register('course', CourseView, basename='courses')
router.register('learning', LearningTechnologyView, basename='learnings')
router.register('client', ClientView, basename='users')
router.register('comment', CommentView, basename='comments')
router.register('publication', PublicationView, 'publications')

urlpatterns = [ 
    path('reg/',RegistrationView.as_view()),
    path('log/',AuthorizationView.as_view()),
    ]

urlpatterns += router.urls
