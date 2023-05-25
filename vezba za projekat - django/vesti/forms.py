

from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm

from .models import *

class  KorisnikCreationUserForm(UserCreationForm):

        class Meta: #definise se da bi se pruzile dodatne informacije o formi
            model = Korisnik  #kaze da je nasa forma povezana sa klasom Korisnik
            #fields = '__all__' #sva polja iz Korisnik ce biti ukljucena u formu
            fields = ['username', 'password1', 'password2']


class KomentarForma(ModelForm):

    class Meta():
        model = Komentar
        exclude = ['autorKomentara', 'zaKnjigu']