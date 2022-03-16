from django.views.generic import ListView, DetailView
from .models import Post
from datetime import datetime


class ProductsList(ListView):
    model = Post
    template_name = 'post.html'
    context_object_name = 'post'
    queryset = Post.objects.order_by('-createTime')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.utcnow()
        return context


class ProductDetail(DetailView):
    model = Post
    template_name = 'news.html'
    context_object_name = 'post'
