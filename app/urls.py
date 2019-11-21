from django.urls import path, include
from rest_framework import routers
from rest_framework.documentation import include_docs_urls
from . import views

router = routers.DefaultRouter()
router.register(r'pedidos', views.PedidoViewSet)
router.register(r'clientes', views.ClienteViewSet)
router.register(r'concessionarias', views.ConcessionariaViewSet)
# router.register(r'groups', views.GroupViewSet)

urlpatterns = [
    path('login-success', views.login_success, name='login_success'),
    path('', views.home, name="home"),
    path('concessionaria/<int:id>', views.concessionaria, name='concessionaria'),
    path('pedido/<int:id>', views.pedido, name='pedido'),
    path('pedido-update/<int:id>/<int:vai>', views.pedidos_update, name='pedido_update'),
    path('api/', include(router.urls)),
    path('docs/', include_docs_urls(title='My API title', public=True))
]