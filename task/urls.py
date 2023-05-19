from django.urls import path
from .views import *

urlpatterns = [
    path("", first_task),
    path("viewCategory", view_category , name = "viewcategory")
]
