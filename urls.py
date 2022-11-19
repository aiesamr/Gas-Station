from . import views
from django.urls import path
from pump.views import IndexTemplateView
from pump.views import FuncionarioCreateView, FuncionarioListView, FuncionarioUpdateView, FuncionarioDeleteView
from pump.views import VeiculoCreateView, VeiculoListView, VeiculoUpdateView, VeiculoDeleteView
from pump.views import BombaCreateView, BombaListView, BombaUpdateView, BombaDeleteView
from pump.views import AbastecimentoCreateView, AbastecimentoListView, AbastecimentoUpdateView, AbastecimentoDeleteView
from pump.views import CompraCreateView, CompraListView, CompraUpdateView, CompraDeleteView




app_name = 'pump'

urlpatterns = [
    path('', IndexTemplateView.as_view(), name='index'),
    path('create-funcionario/', FuncionarioCreateView.as_view(), name='create-funcionario'),
    path('funcionario-list/', FuncionarioListView.as_view(), name='funcionario-list'),
    path('update-funcionario/<pk>', FuncionarioUpdateView.as_view(), name='update-funcionario'),
    path('delete-funcionario/<pk>', FuncionarioDeleteView.as_view(), name='delete-funcionario'),
    path('create-veiculo/', VeiculoCreateView.as_view(), name='create-veiculo'),
    path('veiculo-list/', VeiculoListView.as_view(), name='veiculo-list'),
    path('update-veiculo/<pk>', VeiculoUpdateView.as_view(), name='update-veiculo'),
    path('delete-veiculo/<pk>', VeiculoDeleteView.as_view(), name='delete-veiculo'),
    path('create-bomba/', BombaCreateView.as_view(), name='create-bomba'),
    path('bomba-list/', BombaListView.as_view(), name='bomba-list'),
    path('update-bomba/<pk>', BombaUpdateView.as_view(), name='update-bomba'),
    path('delete-bomba/<pk>', BombaDeleteView.as_view(), name='delete-bomba'),
    path('create-abastecimento/', AbastecimentoCreateView.as_view(), name='create-abastecimento'),
    path('abastecimento-list/', AbastecimentoListView.as_view(), name='abastecimento-list'),
    path('update-abastecimento/<pk>', AbastecimentoUpdateView.as_view(), name='update-abastecimento'),
    path('delete-abastecimento/<pk>', AbastecimentoDeleteView.as_view(), name='delete-abastecimento'),
    path('create-compra/', CompraCreateView.as_view(), name='create-compra'),
    path('compra-list/', CompraListView.as_view(), name='compra-list'),
    path('update-compra/<pk>', CompraUpdateView.as_view(), name='update-compra'),
    path('delete-compra/<pk>', CompraDeleteView.as_view(), name='delete-compra'),

    
]
