URL Maps view Function
<int:id> passes employee ID


from django.urls import path
from . import views

# URL routing for employees app
urlpatterns = [
    path('', views.employee_list, name='employee_list'),
    path('add/', views.employee_create, name='employee_create'),
    path('edit/<int:id>/', views.employee_update, name='employee_update'),
    path('delete/<int:id>/', views.employee_delete, name='employee_delete'),
]
