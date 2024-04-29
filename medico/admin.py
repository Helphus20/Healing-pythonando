from django.contrib import admin
from .models import Especialidades, DadosMedico

# Aqui resgitra-se as models criadas em models.py, para aparecerem no app de admin

admin.site.register(Especialidades)
admin.site.register(DadosMedico)