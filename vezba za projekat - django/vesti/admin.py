from django.contrib import admin

# Register your models here.


from .models import *

admin.site.register(Korisnik)
admin.site.register(Knjiga)
admin.site.register(Komentar)
