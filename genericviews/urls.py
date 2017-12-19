
from django.urls import path
from genericviews import views

app_name = 'genericviews'

urlpatterns = [
    path('', views.IndexView.as_view(), name = 'index'),
    path('<int:pk>', views.DetailsView.as_view(), name = 'detail'),
    path('edit/<int:pk>', views.EditView.as_view(), name = 'edit'),
    path('delete/<int:pk>', views.DeleteView.as_view(), name = 'delete'),
    path('makeentry', views.CreateProductView.as_view(), name = 'makeentry'),
    path('deletemultiple', views.MultipleDeleteView.as_view(), name = 'multiple_delete'),
]
