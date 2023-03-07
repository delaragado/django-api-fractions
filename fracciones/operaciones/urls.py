from django.urls import path

from . import views

urlpatterns = [
    path('suma/', views.SumaFrac, name='index'),
    path('resta/', views.RestaFrac),
    path('multiplicacion/', views.MultiFrac),
    path('division/', views.DivFrac)
,]