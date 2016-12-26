from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy

from .mixins import InstanceOwnerMixin, VerifiedUserMixin

from django.views.generic import (
    CreateView,
    DetailView,
    DeleteView,
    FormView,
    ListView,
    UpdateView
)

from django.db.models import Q
from .models import Posts
from .forms import PostsForm


class PostListView(ListView):
    template_name = 'posts/posts_list.html'
    paginate_by = 8

    def get_queryset(self, *args, **kwargs):
        qs = Posts.objects.filter(privacy='pb')
        if self.request.user.is_authenticated:
            qs = Posts.objects.all()

        query = self.request.GET.get("q", None)
        if query is not None:
            qs = qs.filter(
                Q(content__icontains=query) |
                Q(user__username__icontains=query)
            )
        return qs

    def get_context_data(self, **kwargs):
        context = super(PostListView, self).get_context_data(**kwargs)
        context["form"] = PostsForm
        context["success_url"] = reverse_lazy("posts:list")
        query = self.request.GET.get("q", None)
        if query is not None:
            context["query"] = query
        return context

    def get(self, request, *args, **kwargs):
        return super(PostListView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        form = PostsForm(request.POST)
        return self.form_valid(form)

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        form.save()
        return HttpResponseRedirect("/")


class PostCreateView(LoginRequiredMixin, VerifiedUserMixin, CreateView):
    form_class = PostsForm
    success_url = reverse_lazy("posts:list")
    template_name = 'posts/create.html'
    login_url = reverse_lazy('users:login')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(PostCreateView, self).form_valid(form)


class PostDetailView(DetailView):
    queryset = Posts.objects.all()
    template_name = 'posts/detail.html'


class PostDeleteView(LoginRequiredMixin, InstanceOwnerMixin, DeleteView):
    model = Posts
    success_url = reverse_lazy("posts:list")
    template_name = 'posts/delete.html'
    login_url = reverse_lazy('users:login')


class PostUpdateView(LoginRequiredMixin, InstanceOwnerMixin, UpdateView):
    queryset = Posts.objects.all()
    form_class = PostsForm
    template_name = 'posts/update.html'
    login_url = reverse_lazy('users:login')
