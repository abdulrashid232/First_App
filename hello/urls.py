from django.urls import path

from . import views

urlpatterns = [
    path("",views.index, name="index"),
    # path("abdel",views.abdel, name="abdel"),
    path("<str:name>",views.greet, name="greet")
    
]
