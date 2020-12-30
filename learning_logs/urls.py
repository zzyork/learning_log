"""定义learning_logs的URL模式"""

from django.urls import path
from learning_logs import views

urlpatterns = [
    path('', views.index, name='index'),
    path('topic/', views.topics, name='topics'),
    path('topics/<topic_id>', views.topic, name='topic'),
    path('new_topic/', views.new_topic, name='new_topic'),
    path('new_entry/<topic_id>/', views.new_entry, name='new_entry'),
    path('edit_entry/<entry_id>/', views.edit_entry, name='edit_entry'),
]