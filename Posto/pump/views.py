from django.shortcuts import render
from django.views.generic import CreateView, TemplateView, ListView, UpdateView, DeleteView, DetailView, View
from django.urls.base import reverse_lazy
from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect
from .models import Funcionario, Veiculo, Bomba, Abastecimento, CompraCombustivel
from .forms import FuncionarioForm, VeiculoForm, BombaForm, AbastecimentoForm, CompraCombForm


class IndexTemplateView(TemplateView):
    template_name = 'index.html'

class FuncionarioCreateView(CreateView):
    template_name = 'create-funcionario.html'
    model = Funcionario
    form_class = FuncionarioForm
    success_url = reverse_lazy('pump:funcionario-list')

    def create_funcionario(request):
        if request.method == 'POST':
            form = FuncionarioForm(request.POST)
            if form.is_valid():
                form.save()
        else:
            form = FuncionarioForm()
            return render(request, 'create-funcionario.html', {'form' : form})


class FuncionarioListView(ListView):
    template_name = 'funcionario-list.html'
    model = Funcionario
    paginate_by = 10
    context_object_name = 'funcionarios'

    def get_queryset(self):
        query = self.request.GET.get('search') 
        if query:
            return Funcionario.objects.filter(coren__icontains=query)
        else: 
            return Funcionario.objects.all().order_by()


class FuncionarioUpdateView(UpdateView):
    template_name = 'update-funcionario.html'
    model = Funcionario
    fields = '__all__'
    context_object_name = 'funcionario'
    success_url = reverse_lazy('pump:funcionario-list')



class FuncionarioDeleteView(DeleteView):
    template_name = "delete-funcionario.html"
    model = Funcionario
    fields = '__all__'
    context_object_name = 'funcionario'
    success_url = reverse_lazy('pump:funcionario-list')



class VeiculoCreateView(CreateView):
    template_name = 'create-veiculo.html'
    model = Veiculo
    form_class = VeiculoForm
    success_url = reverse_lazy('pump:veiculo-list')

    def create_veiculo(request):
        if request.method == 'POST':
            form = VeiculoForm(request.POST)
            if form.is_valid():
                form.save()
        else:
            form = VeiculoForm()
            return render(request, 'create-veiculo.html', {'form' : form})


class VeiculoListView(ListView):
    template_name = 'veiculo-list.html'
    model = Veiculo
    paginate_by = 10
    context_object_name = 'veiculos'

    def get_queryset(self):
        query = self.request.GET.get('search') 
        if query:
            return Veiculo.objects.filter(coren__icontains=query)
        else: 
            return Veiculo.objects.all().order_by()


class VeiculoUpdateView(UpdateView):
    template_name = 'update-veiculo.html'
    model = Veiculo
    fields = '__all__'
    context_object_name = 'veiculos'
    success_url = reverse_lazy('pump:veiculo-list')



class VeiculoDeleteView(DeleteView):
    template_name = "delete-veiculo.html"
    model = Veiculo
    fields = '__all__'
    context_object_name = 'veiculo'
    success_url = reverse_lazy('pump:veiculo-list')


class BombaCreateView(CreateView):
    template_name = 'create-bomba.html'
    model = Bomba 
    form_class = BombaForm
    success_url = reverse_lazy('pump:bomba-list')

    def create_bomba(request):
        if request.method == 'POST':
            form = BombaForm(request.POST)
            if form.is_valid():
                form.save()
        else:
            form = BombaForm()
            return render(request, 'create-bomba.html', {'form' : form})


class BombaListView(ListView):
    template_name = 'bomba-list.html'
    model = Bomba
    paginate_by = 10
    context_object_name = 'bombas'

    def get_queryset(self):
        query = self.request.GET.get('search') 
        if query:
            return Bomba.objects.filter(coren__icontains=query)
        else: 
            return Bomba.objects.all().order_by()


class BombaUpdateView(UpdateView):
    template_name = 'update-bomba.html'
    model = Bomba
    fields = '__all__'
    context_object_name = 'bombas'
    success_url = reverse_lazy('pump:bomba-list')



class BombaDeleteView(DeleteView):
    template_name = "delete-bomba.html"
    model = Bomba
    fields = '__all__'
    context_object_name = 'bombas'
    success_url = reverse_lazy('pump:bomba-list')



class AbastecimentoCreateView(CreateView):
    template_name = 'create-abastecimento.html'
    model = Abastecimento 
    form_class = AbastecimentoForm
    success_url = reverse_lazy('pump:abastecimento-list')

    def create_abastecimento(request):
        if request.method == 'POST':
            form = AbastecimentoForm(request.POST)
            if form.is_valid():
                form.save()
        else:
            form = AbastecimentoForm()
            return render(request, 'create-bomba.html', {'form' : form})


class AbastecimentoListView(ListView):
    template_name = 'abastecimento-list.html'
    model = Abastecimento
    paginate_by = 10
    context_object_name = 'abastecimentos'

    def get_queryset(self):
        query = self.request.GET.get('search') 
        if query:
            return Abastecimento.objects.filter(coren__icontains=query)
        else: 
            return Abastecimento.objects.all().order_by()


class AbastecimentoUpdateView(UpdateView):
    template_name = 'update-abastecimento.html'
    model = Abastecimento
    fields = '__all__'
    context_object_name = 'abastecimentos'
    success_url = reverse_lazy('pump:abastecimento-list')



class AbastecimentoDeleteView(DeleteView):
    template_name = "delete-abastecimento.html"
    model = Abastecimento
    fields = '__all__'
    context_object_name = 'abastecimentos'
    success_url = reverse_lazy('pump:abastecimento-list')



class CompraCreateView(CreateView):
    template_name = 'create-compra.html'
    model = CompraCombustivel 
    form_class = CompraCombForm
    success_url = reverse_lazy('pump:compra-list')

    def create_compra(request):
        if request.method == 'POST':
            form = CompraCombForm(request.POST)
            if form.is_valid():
                form.save()
        else:
            form = CompraCombForm()
            return render(request, 'create-compra.html', {'form' : form})


class CompraListView(ListView):
    template_name = 'compra-list.html'
    model = CompraCombustivel
    paginate_by = 10
    context_object_name = 'compras'

    def get_queryset(self):
        query = self.request.GET.get('search') 
        if query:
            return CompraCombustivel.objects.filter(coren__icontains=query)
        else: 
            return CompraCombustivel.objects.all().order_by()


class CompraUpdateView(UpdateView):
    template_name = 'update-compra.html'
    model = CompraCombustivel
    fields = '__all__'
    context_object_name = 'compras'
    success_url = reverse_lazy('pump:compra-list')



class CompraDeleteView(DeleteView):
    template_name = "delete-compra.html"
    model = CompraCombustivel
    fields = '__all__'
    context_object_name = 'compras'
    success_url = reverse_lazy('pump:compra-list')


