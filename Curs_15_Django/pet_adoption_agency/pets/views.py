from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import Pet
from django.urls import reverse, reverse_lazy
from django.views import generic


# Create your views here.

# view este functia care va genera ce se va afisa in pagina web.

# def index(request):
#     return HttpResponse("Hello from pets_index")
#
#
# def pets(request):
#     pets_list = Pet.objects.all()  # ORM prin care accesam direct baza de date
#     return render(request, 'all_pets.html', {"pets": pets_list})
#
#
# def pet_detail(request, pet_id):
#     pet = get_object_or_404(Pet, pk=pet_id)
#     return render(request, 'pet_detail.html', {'pet': pet})
#
#
def error_404(request, exception):
    return render(request, 'error.html', {'error_message': 'Eroare'})
#
# def pet_add(request):
#     pet_details = request.POST.dict()
#     try:
#         pet = Pet(name=pet_details['name'], gender=pet_details['gender'],
#                   age=pet_details['age'], species=pet_details['species'])
#         pet.save()
#     except KeyError:
#         return render(request, 'error.html', {'error_message': 'Invalid pet details'})
#     return HttpResponseRedirect(reverse('pets:all_pets'))

class PetsView(generic.ListView):
    template_name = 'all_pets.html'
    context_object_name = 'pets'

    def get_queryset(self):
        return Pet.objects.all()


class PetDetailView(generic.DetailView):
    model = Pet
    template_name = 'pet_detail.html'

class PetCreateVeiew(generic.CreateView):
    model = Pet
    fields = ['name','age','gender','species']
    success_url = reverse_lazy('pets:all_pets') #reverse_lazy asteapta pana in ultima secunda
    #ca sa faca operatiunea ceruta, doar daca e necesar