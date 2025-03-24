from django.urls import path
from .views import DonorListCreateView, DonorDeleteView

urlpatterns = [
    path('donors/', DonorListCreateView.as_view(), name='donor-list-create'),  # GET & POST
    path('donors/<int:pk>/', DonorDeleteView.as_view(), name='donor-delete'),  # DELETE
]
