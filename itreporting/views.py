from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Issue
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


# Create your views here.
def home(request):
    return render(request, 'itreporting/home.html', {'title': 'Home'})

def about(request):
    return render(request, 'itreporting/about.html',  {'title': 'About Us'})

def report(request):
    daily_report= {
        'issues': Issue.objects.all()
    }

    return render(request, 'itreporting/report.html', daily_report)

def contact(request):
    return render(request, 'itreporting/contact.html', {'title': 'Contact Us'})

class PostListView(ListView):
    model = Issue
    template_name = 'itreporting/report.html'
    context_object_name = 'issues'
    ordering = ['-date_submitted']
    paginate_by = 5

class PostDetailView(DetailView):
    model = Issue

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Issue
    fields = ['type', 'room', 'details']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Issue
    fields = ['type', 'room', 'details']


    def test_func(self):
        issue = self.get_object()
        if self.request.user == issue.author:
            return True
        return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Issue
    success_url = '/report'

    def test_func(self):
        issue = self.get_object()
        if self.request.user == issue.author:
                return True
        return False

class UserPostListView(ListView):
    model = Issue
    template_name = 'itreporting/user_issues.html'
    context_object_name = 'issues'
    paginate_by = 5

    def get_queryset(self):
        user=get_object_or_404(User, 
        username=self.kwargs.get('username'))
        return Issue.objects.filter(author=user).order_by('-date_submitted')