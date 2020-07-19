from django.urls import path

from blog import views
app_name = 'blog'
urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('<int:pk>/<slug:slug>', views.post_detail, name='post_detail'),
    path('category/<slug:slug>', views.post_by_category, name='post_by_category'),
    path('tag/<slug:slug>', views.post_by_tag, name='post_by_tag'),

]
