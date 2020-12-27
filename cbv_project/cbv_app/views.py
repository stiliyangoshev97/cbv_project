from django.shortcuts import render
from django.views.generic import View, TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from cbv_app.models import Song, Detail

# Create your views here.

class index(TemplateView):
	template_name = 'cbv_app/index.html'

class SongListView(ListView):
	model = Song
	context_object_name = 'songs'


class SongDetailView(DetailView):
	model = Song
	context_object_name = 'song_detail'
	template_name = "cbv_app/song_detail.html"


class SongCreateView(CreateView):
	model = Song
	fields = ('name', 'artist', 'year')


class SongUpdateView(UpdateView):
	model = Song
	fields = ('name', 'artist')


class SongDeleteView(DeleteView):
	model = Song
	success_url = reverse_lazy('cbv_app:list')