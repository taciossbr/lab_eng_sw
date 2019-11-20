from django.urls import path
from . import views


urlpatterns = [
    path('login-success', views.login_success, name='login_success'),
    path('', views.home, name="home"),
    path('concessionaria/<int:id>', views.concessionaria, name='concessionaria'),
    path('pedido/<int:id>', views.pedido, name='pedido')
]