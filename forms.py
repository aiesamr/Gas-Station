from django import forms
from .models import Funcionario, Veiculo, Bomba, Abastecimento, CompraCombustivel


class FuncionarioForm(forms.ModelForm):

    class Meta:
        model = Funcionario
        fields = '__all__'
        

class VeiculoForm(forms.ModelForm):

    class Meta:
        model = Veiculo
        fields = '__all__'


class BombaForm(forms.ModelForm):

    class Meta:
        model = Bomba
        fields = '__all__'

class AbastecimentoForm(forms.ModelForm):

    class Meta:
        model = Abastecimento
        fields = '__all__'

class CompraCombForm(forms.ModelForm):

    class Meta:
        model = CompraCombustivel
        fields = '__all__'