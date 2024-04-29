from django.urls import path
from . import views

#toda url precisa ficar dentro de urlpatterns. Toda pagina dentro do app recebe uma url diferente, e aqui organizamos as rotas
urlpatterns = [
    path('cadastro/', views.cadastro, name="cadastro"),
    path('login/', views.login, name="login"),
    path('logout/', views.logout, name="logout")
]
