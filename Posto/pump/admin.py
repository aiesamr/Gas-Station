from django.contrib import admin

from .models import Funcionario, Veiculo, Bomba, Abastecimento, CompraCombustivel

admin.site.register(Funcionario)
admin.site.register(Veiculo)
admin.site.register(Bomba)
admin.site.register(Abastecimento)
admin.site.register(CompraCombustivel)


