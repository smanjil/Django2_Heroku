
from django.urls import path
from genericviews import views

app_name = 'genericviews'

urlpatterns = [
    path('', views.IndexView.as_view(), name = 'index'),
    path('<int:pk>', views.DetailsView.as_view(), name = 'detail'),
    path('makeentry', views.makeentry, name = 'makeentry')
]
