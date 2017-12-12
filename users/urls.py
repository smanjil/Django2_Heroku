
from django.urls import path
from users import views

app_name = 'users'

urlpatterns = [
    path('create', views.RegisterView.as_view(), name = 'register'),
    path('login', views.LoginView.as_view(), name = 'login'),
    path('reset', views.ResetPasswordView.as_view(), name = 'reset'),
    path('logout', views.logout_user, name = 'logout')
]
