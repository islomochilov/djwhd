from django.urls import path
from .views import ContactlistAPIView,ContactCreateAPIView,ContactUpdateAPIlist,\
    ContactDeleteAPIView,ContactDetailAPIView,ContactMixedAPIView



urlpatterns=[
    path('contact/',ContactlistAPIView.as_view(),name='contact_list'),
    path('contact/create/',ContactCreateAPIView.as_view(),name='contact_create'),
    path('contact/update/<int:pk>/',ContactUpdateAPIlist.as_view(),name='contact_update'),
    path('contact/delete/<int:pk>/',ContactDeleteAPIView.as_view(),name='contact_delete'),
    path('contact/detail/<int:pk>/',ContactDetailAPIView.as_view(),name='contact_detail'),
    path('contact/mixed/<int:pk>/',ContactMixedAPIView.as_view(),name='contact_mixed')
]