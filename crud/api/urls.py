from django.urls import URLPattern,path
from api import views

urlpatterns = [
    path('get/data',views.get_data),
    path('class/data',views.ListViews.as_view())
]