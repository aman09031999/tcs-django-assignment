from django.urls import path
from django.conf.urls import url, include
from . import views

# Create your urls here.
urlpatterns = [
    path('/', views.home, name='home'),
    path('/add', views.add, name='add'),
    path('/view', views.view, name='view'),
    path('/<int:id>/edit', views.edit),
    path('/<int:id>/update', views.update, name='update'),
    path('/<int:id>/delete', views.delete, name='delete')
]