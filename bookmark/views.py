from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy
from .models import Bookmark

# Create your views here.
class BookmarkListView(ListView) :
    model = Bookmark
    paginate_by = 5

class BookmarkCreateView(CreateView) :
    model = Bookmark
    fields = ['site_name', 'url']
    success_url = reverse_lazy('list') # 북마크 url에서 name이 list인 것을 찾아 거기 있는 view로 이동
    template_name_suffix = '_create' # bookmark_create.html 화면을 찾아가라는 의미

class BookmarkDetailView(DetailView) :
    model = Bookmark

class BookmarkUpdateView(UpdateView) :
    model = Bookmark
    fields = ['site_name', 'url']
    template_name_suffix = '_update'
    # 여기에는 success_url이 없어 업데이트 버튼을 누른 후 어디로 갈 지 정해져 있지 않음
    # 이럴 경우 models 파일에 정의해놓은 get_absolute_url 메소드로 감
    # get_absolute_url 메소드에는 detail 화면으로 가라는 지시가 있음
    # detail 화면으로 가게 됨

class BookmarkDeleteView(DeleteView) :
    model = Bookmark
    success_url = reverse_lazy('list')