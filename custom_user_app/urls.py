from django.urls import path
from .views import SignUpView

urlspatterns = [
    path('signup/', SignUpView, name='signup')
]
