from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Grade
from .forms import GradeForm
from django.db.models import Q
from django.urls import reverse_lazy

class GradeListView(ListView):
    model = Grade
    template_name = 'grades/grades_list.html'
    context_object_name = 'grades'
    paginate_by = 5

    def get_queryset(self):
        queryset = super().get_queryset()
        
        # 获取搜索参数
        search = self.request.GET.get('search', '')
        
        # 获取排序参数
        sort_by = self.request.GET.get('sort', 'grade_number')  # 默认按班级编号排序
        sort_dir = self.request.GET.get('dir', 'asc')  # 默认升序
        
        # 应用搜索过滤
        if search:
            queryset = queryset.filter(
                Q(grade_name__icontains=search) |
                Q(grade_number__icontains=search)
            )
        
        # 应用排序
        if sort_dir == 'desc':
            sort_by = f'-{sort_by}'  # 降序前缀为 -
        
        queryset = queryset.order_by(sort_by)
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # 添加排序参数到上下文
        context['current_sort'] = self.request.GET.get('sort', 'grade_number')
        context['current_dir'] = self.request.GET.get('dir', 'asc')
        return context


class GradeCreateView(CreateView):
    model = Grade
    form_class = GradeForm
    template_name = 'grades/grade_form.html'
    success_url = reverse_lazy('grades_list')


class GradeUpdateView(UpdateView):
    model = Grade
    template_name = 'grades/grade_form.html'
    form_class = GradeForm
    success_url = reverse_lazy('grades_list')


class GradeDeleteView(DeleteView):
    model = Grade
    template_name = 'grades/grade_delete_confirm.html'
    success_url = reverse_lazy('grades_list')