from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index')
]
handler404 = 'weather.views.pageNotFound'
# handler500 = 'weather.views.serverError'