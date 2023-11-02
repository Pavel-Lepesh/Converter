from django.urls import path
from .views import view_base_page


urlpatterns = [
    path('', view_base_page, name='view_base_page')
]
