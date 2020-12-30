"""定义learning_logs的URL模式"""

from django.urls import path
from learning_logs import views

urlpatterns = [
    path('', views.index, name='index'),
    path('topic/', views.topics, name='topics'),
    path('topics/<topic_id>', views.topic, name='topic'),
]