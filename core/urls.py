from django.urls import path
from core import views


urlpatterns = [
    path('', views.IndexView.as_view(), name='home'),
    path('add/categoria', views.CategoriaCreateView.as_view(),
         name='addCategoria'),
    path('listar/categoria', views.CategoriaListView.as_view(),
         name='listarCategorias'),
    path('atualizar/categoria/<int:pk>', views.CategoriaUpdateView.as_view(),
         name='atualizaCategoria'),
    path('excluir/categoria/<int:pk>', views.CategoriaDeleteView.as_view(),
         name='excluiCategoria'),

    path('add/produto', views.ProdutoCreateView.as_view(),
         name='addProduto'),
    path('listar/produto', views.ProdutoListView.as_view(),
         name='listarProdutos'),
    path('atualizar/produto/<int:pk>', views.ProdutoUpdateView.as_view(),
         name='atualizaProduto'),
    path('excluir/produto/<int:pk>', views.ProdutoDeleteView.as_view(),
         name='excluiProduto'),
]