from django.urls import URLPattern,path
from session import views

urlpatterns = [
    path('get/data',views.get_data),
    path('class/data',views.ListViews.as_view())
]