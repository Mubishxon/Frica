from django.urls import path
from .views import index, computer, contact, mans_clothes, womans_clothes, fdetail, kdetail, bdetail, cdetail, Computerdetail, ComputerUpdateView, ComputerDeleteView, ComputerCreateView
urlpatterns = [
    path('', index, name='index'),
    path('computer/', computer, name='computer'),
    path('contact/', contact, name='contact'),
    path('mans_clothes/', mans_clothes, name='mans_clothes'),
    path('womans_clothes/', womans_clothes, name='womans_clothes'),
    path('fdetail/<int:id>/', fdetail, name='fdetail'),
    path('kdetail/<int:id>/', kdetail, name='kdetail'),
    path('bdetail/<int:id>/', bdetail, name='bdetail'),
    path('cdetail/<int:id>/', cdetail, name='cdetail'),
    path('computerdetail/<slug:computers>/', Computerdetail, name='computerdetail'),
    path('computer/edit/<slug>/', ComputerUpdateView.as_view(), name='computerUpdate'),
    path('computers/delete/<slug>/', ComputerDeleteView.as_view(), name='computerDelete'),
    path('computers/create', ComputerCreateView.as_view(), name='computerCreate'),
]