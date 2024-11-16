from django.contrib import admin
from .models import comensal
from .models import mesa
from .models import reserva
from .models import personal
from .models import mesero
from .models import cocinero
from .models import menu
from .models import plato
from .models import prepara
from .models import ingrediente
from .models import ingredientes_plato
from .models import pedido
from .models import pago
# Register your models here.
admin.site.register(comensal)
admin.site.register(mesa)
admin.site.register(reserva)
admin.site.register(personal)
admin.site.register(mesero)
admin.site.register(cocinero)
admin.site.register(menu)
admin.site.register(plato)
admin.site.register(prepara)
admin.site.register(ingrediente)
admin.site.register(ingredientes_plato)
admin.site.register(pedido)
admin.site.register(pago)