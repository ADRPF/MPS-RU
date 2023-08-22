from django.contrib import admin
from .models import Pessoa
from .models import Pedido
from .models import Prato
from .models import Cardapio

admin.site.register(Pessoa)
admin.site.register(Pedido)
admin.site.register(Cardapio)
admin.site.register(Prato)

