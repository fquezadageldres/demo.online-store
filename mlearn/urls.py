from django.urls import path
from .views.p003 import P003

urlpatterns = [
    path('p003/',P003.as_view(), name="p003"),
    path('p003/p003_predict', P003.p003Predict, name="p003_predict"),
]