from django.urls import path
from cbv_app import views
from django.conf.urls import url

app_name = 'cbv_app'

urlpatterns = [

    path('', views.SongListView.as_view(), name = 'list'),
    url('^(?P<pk>\d+)/$', views.SongDetailView.as_view(), name = 'detail'),
    #path('<int:id>/', views.SongDetailView.as_view(), name = 'detail'),
    path('create/', views.SongCreateView.as_view(), name = 'create'),
    url('^update/(?P<pk>\d+)/$', views.SongUpdateView.as_view(), name = 'update'),
    url('^delete/(?P<pk>\d+)/$', views.SongDeleteView.as_view(), name = 'delete'),


]