from django.urls import path
from .import views

urlpatterns = [
    path('', views.home, name='home'),
    path('', views.home, name='arrow'),
    path('add_student/', views.add_student, name='add_student'),
    path('about/', views.about, name='about'),
    path('profile/<int:id>', views.profile, name='profile'),
    path('update/<int:id>', views.update, name='update'),
    path('delete/<int:id>', views.delete, name='delete'),
    path('filter/', views.filter, name='filter'),
    path('filter/', views.filter, name='refresh'),
    path('import_csv/', views.import_csv, name='import_csv'),
    path('export/', views.export, name='export'),
]