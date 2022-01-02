from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:project_id>', views.show, name='show'),
    path('documents', views.index_documents, name='index_documents'),
    path('documents/<int:pk>', views.show_document, name='show_document'),
    path('documents/new', views.new_document, name='new_document'),
]