# Generated by Django 4.2 on 2023-05-25 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vesti', '0002_knjiga_slika'),
    ]

    operations = [
        migrations.AddField(
            model_name='knjiga',
            name='brojOcena',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='knjiga',
            name='ocena',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=5),
        ),
    ]
