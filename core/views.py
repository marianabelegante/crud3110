from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, ListView, UpdateView, DeleteView

from core.models import Categoria, Produto


class IndexView(TemplateView):
    template_name = 'index.html'


class CategoriaCreateView(CreateView):
    model = Categoria
    template_name = 'categoria/formcategoria.html'
    fields = ['descricao']
    success_url = reverse_lazy('home')


class CategoriaListView(ListView):
    model = Categoria
    template_name = 'categoria/listarcategorias.html'
    queryset = Categoria.objects.order_by('descricao').all()
    context_object_name = 'categorias'

class CategoriaUpdateView(UpdateView):
    model = Categoria
    template_name = 'categoria/formcategoria.html'
    fields = ['descricao']
    success_url = reverse_lazy('listarCategorias')

class CategoriaDeleteView(DeleteView):
    model = Categoria
    template_name = 'categoria/delcategoria.html'
    success_url = reverse_lazy('listarCategorias')
    context_object_name = 'categoria'







class ProdutoCreateView(CreateView):
    model = Produto
    template_name = 'produto/formproduto.html'
    fields = ['nome', 'descricao', 'preco', 'categoria']
    success_url = reverse_lazy('home')

class ProdutoListView(ListView):
    model = Produto
    template_name = 'produto/listarproduto.html'
    queryset = Produto.objects.order_by('nome').all()
    context_object_name = 'produtos'

class ProdutoUpdateView(UpdateView):
    model = Produto
    template_name = 'produto/listarproduto.html'
    fields = ['nome', 'descricao', 'preco', 'categoria']
    success_url = reverse_lazy('listarProdutos')

class ProdutoDeleteView(DeleteView):
    model = Produto
    template_name = 'produto/delproduto.html'
    success_url = reverse_lazy('listarProdutos')
    context_object_name = 'produto'
