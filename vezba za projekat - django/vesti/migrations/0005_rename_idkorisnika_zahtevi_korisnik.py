# Generated by Django 4.2.1 on 2023-05-26 13:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vesti', '0004_zahtevi'),
    ]

    operations = [
        migrations.RenameField(
            model_name='zahtevi',
            old_name='idKorisnika',
            new_name='korisnik',
        ),
    ]
