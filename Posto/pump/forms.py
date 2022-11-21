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
    def clean(self):
        super(forms.ModelForm, self).clean()

        qtd_litros = self.cleaned_data.get('qtd_litro')
        tipoGasForm = self.cleaned_data.get('tipoGas')
        km_odometroForm = self.cleaned_data.get('km_odometro')
        placaForm = self.cleaned_data.get('placa')

        try:
            km_odometro_anterior = list(Abastecimento.objects.filter(placa=placaForm).values())[-1]['km_odometro']
        except:
            km_odometro_anterior=None
        try:
            em_estoque = list(Bomba.objects.filter(tipo_combustivel=tipoGasForm).values())[0]['qtdd_estoque']
        except:
            em_estoque =0
        if em_estoque==0 or em_estoque ==None:
            raise forms.ValidationError('Sem Estoque!')

        if qtd_litros > em_estoque:
            raise forms.ValidationError(
                'Quantidade de litros insuficente no estoque!')
        if km_odometro_anterior != None:
            if km_odometroForm <= km_odometro_anterior:
                raise forms.ValidationError(
                    'Kilometragem abaixo do registro anterior')

        # return any errors if found
        return self.cleaned_data

class CompraCombForm(forms.ModelForm):

    class Meta:
        model = CompraCombustivel
        fields = '__all__'