from django.urls import path
from . import views

urlpatterns = [#toda url precisa ficar dentro de urlpatterns
    path('cadastro/', views.cadastro, name="cadastro")
]
