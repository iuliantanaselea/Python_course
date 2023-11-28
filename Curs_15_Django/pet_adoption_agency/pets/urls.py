from django.conf.urls.static import static
from django.urls import path
from . import views

# from . -> din folderul curent

app_name = 'pets'
# urlpatterns = [
#     path('', views.pets, name='all_pets'),
#     path('<int:pet_id>/', views.pet_detail, name='pet_detail'), #vom avea un /pets/id
#     path('pet/', views.pet_add, name='add')
# ]
urlpatterns = [
    path('', views.PetsView.as_view(), name='all_pets'),
    path('<int:pk>/', views.PetDetailView.as_view(), name='pet_detail'), #vom avea un /pets/id
    path('pet/', views.PetCreateVeiew.as_view(), name='add')

] + static('static')

