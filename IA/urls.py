from django.urls import path
from . import views


app_name = 'IA'

urlpatterns = [
    path('', views.index, name='index'),
    path('main/', views.main, name='main'),
    path('search/', views.search, name="search"),
    path('on_demand/',views.on_demand, name='on_demand'),
    path('show_hostels/<hostel_id>', views.show_hostels, name='show_hostels'),
    path('about_us', views.about_us, name='about_us'),
    path('contact_us', views.contact_us, name='contact_us'),
    path('add', views.add, name='add'),
    path('update_hostels/<hostel_id>', views.update_hostels, name='update_hostels'),
    path('admin_page', views.admin_page, name='admin_page'),
    path('list_hostels', views.list_hostels, name='list_hostels'),
    path('delete_hostels/<hostel_id>', views.delete_hostels, name='delete_hostels'),
    path('contact_forms/<c_id>', views.contact_forms, name='contact_forms'),
    path('list_contacts', views.list_contacts, name='list_contacts'),
    path('demand_forms/<d_id>', views.demand_forms, name='demand_forms'),
    path('list_demands', views.list_demands, name='list_demands'),
]