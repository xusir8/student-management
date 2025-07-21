from django.urls import path
from .views import GradeListView, GradeCreateView, GradeUpdateView, GradeDeleteView

urlpatterns = [
    path('create/', GradeCreateView.as_view(), name='grade_create'),
    path('<int:pk>/update/', GradeUpdateView.as_view(), name='grade_update'),
    path('<int:pk>/delete/', GradeDeleteView.as_view(), name='grade_delete'),
    path('', GradeListView.as_view(), name='grades_list'),
]