from django.urls import path, re_path

from . import views

urlpatterns = [
    path("", views.index, name="middlewares"),
    re_path(r"^calc", views.calc)
]