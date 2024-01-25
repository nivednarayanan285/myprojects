from django.urls import path,include
from .views import *

urlpatterns = [
    path('',home,name='home'),
    path('departments/',departments,name='departments'),
    path('booking/',booking,name='booking'),
    path('doctors/',doctors,name='doctors'),
    path('contact/',contact,name='contact'),
    path('about/',about,name='about'),

    path('docdetailview/<int:pk>',DocDetailView.as_view(),name='docdetailview')


]
