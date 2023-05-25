from django.db import models
from decimal import Decimal
# Create your models here.

from django.contrib.auth.models import User, AbstractUser

class Korisnik(AbstractUser):
    br_knjiga = models.IntegerField(default=0);

class Knjiga(models.Model):
    autor = models.ForeignKey(Korisnik, on_delete=models.CASCADE)
    ime = models.CharField(max_length=50)
    opis = models.CharField(max_length=1000)
    pdf_file = models.FileField(upload_to='books/')
    slika = models.ImageField(upload_to='books_images/', blank=True, null=True)
    ocena = models.DecimalField(max_digits=5, decimal_places=2, default=Decimal('0'))
    brojOcena = models.IntegerField(default=0)


    def prosecnaOcena(self):
        if self.brojOcena != 0:
            #return  self.ocena / self.brojOcena
            return self.ocena / Decimal(self.brojOcena)
        else:
            return 0

    class Meta:
        db_table = 'Knjiga'


class Komentar(models.Model):
    autorKomentara = models.ForeignKey(Korisnik, on_delete=models.CASCADE)
    zaKnjigu = models.ForeignKey(Knjiga, on_delete=models.CASCADE)
    tekst = models.CharField(max_length=300)

    class Meta:
        db_table = 'Komentar'