
from django.shortcuts import render

# Create your views here.


from django.shortcuts import render, redirect
from .models import Korisnik, Knjiga


def add_user(request):
    if(request.method == 'POST'):
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']

        korisnik = Korisnik(username=username, password=password, email=email)
        korisnik.save()

        return redirect("add_book")
    return render(request, 'add_user.html')




def add_book(request):
    if (request.method == 'POST'):
        ime = request.POST['ime']
        opis = request.POST['opis']
        autor_id = request.POST['autor_id']
        pdf_file = request.FILES['pdf_file']
        slika = request.FILES.get('image')

        autor = Korisnik.objects.get(id=autor_id)

        new_knjiga = Knjiga(ime=ime, opis=opis, autor=autor, pdf_file=pdf_file, slika=slika)

        new_knjiga.save()

        return redirect('book_list')
    return render(request, 'add_book.html')


def book_list(request):
    books = Knjiga.objects.all()
    comments = Komentar.objects.all()
    context = {
        'books': books,
        'comments': comments
    }
    return render(request, 'book_list.html', context)


def delete_all_books(request):
    Knjiga.objects.all().delete()
    return redirect('book_list')

from django.contrib.auth import login,authenticate
from django.contrib.auth.forms import AuthenticationForm

"""def login_req(request):
    form = AuthenticationForm(request=request, data=request.POST or None) #loginovani user se stavlja u session storage
    if form.is_valid():
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(username=username, password=password)
        if user:
            login(request, user) #ubaci usera u session storage
            return redirect("book_list")    #redirect radi po stringovima, iz urls polje name

    context = {
        'form': form
    }
    return render(request, 'registration/login.html',context)"""

def login_req(request):
    if request.method == 'POST':
        username = request.POST['username'] #pristupa po parametru name
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user:
            login(request, user)  # ubaci usera u session storage
            return redirect("book_list")  # redirect radi po stringovima, iz urls polje name

    return render(request, 'HTML/login.html')

from django.contrib.auth import logout

def logout_req(request):
    #iz session storage-a obrise user-a
    logout(request)
    return redirect('login')



"""from django.contrib.auth.forms import UserCreationForm
from .forms import KorisnikCreationUserForm
def registration(request):
    form = KorisnikCreationUserForm(data=request.POST or None)
    if form.is_valid():
        user = form.save()
        login(request, user)
        return redirect('book_list')
    context = {
        'form': form
    }
    return  render(request, 'registration/registration.html', context ) """

from django.contrib.auth.hashers import make_password

def registration(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = make_password(request.POST['password'])
        firstName = request.POST['firstName']
        lastName = request.POST['lastName']
        email = request.POST['email']

        korisnik = Korisnik(username=username, password=password, first_name=firstName, last_name=lastName, email=email)

        korisnik.save()
        login(request, korisnik)
        return redirect('book_list')
    return render(request, 'HTML/registracija.html')

from .forms import *
from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
def addComment(request):
    if request.method == 'POST':
        sadrzajKomentara = request.POST['comment']
        autorKomentara = Korisnik.objects.get(username=request.user.get_username())
        idKnjige = request.POST['book_id']
        objekatKnjige = Knjiga.objects.get(id=idKnjige)

        komentar = Komentar(autorKomentara=autorKomentara, tekst=sadrzajKomentara, zaKnjigu=objekatKnjige)

        komentar.save()
    return redirect('book_list')

def addCommentPage(request, book_id):
    return render(request, 'add_comment_page.html', {'book_id': book_id})


from decimal import Decimal

def rateBook(request):
    if request.method == 'POST':
        idKnjige = request.POST['book_id_rate']
        ocena = Decimal(request.POST['ocena'])

        knjiga = Knjiga.objects.get(id=idKnjige)

        knjiga.brojOcena += 1
        knjiga.ocena += ocena

        knjiga.save()

    return redirect('book_list')

def rateBookPage(request, book_id_rate):
    return render(request, 'rate_book_page.html', {'book_id_rate': book_id_rate})



def showCommentsForBook(request):
    book_id = request.POST['book_id_comment']
    comments = Komentar.objects.filter(zaKnjigu__id=book_id)    # __ omogucava da pristupimo poljima datog stranog kljuca
    bookTitle = comments[0].zaKnjigu.ime
    context = {
        'comments': comments,
        'bookTitle': bookTitle
    }
    return render(request, 'comments_for_book.html', context)

















