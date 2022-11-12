# Generated by Django 4.0.1 on 2022-11-09 21:12

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('commande', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='commande',
            options={'ordering': ['-date_commande']},
        ),
        migrations.AlterField(
            model_name='commande',
            name='date_commande',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name='Date de Commande'),
        ),
        migrations.AlterField(
            model_name='commande',
            name='ecart',
            field=models.IntegerField(default=0, verbose_name='Ecart'),
        ),
        migrations.AlterField(
            model_name='commande',
            name='quantite_commande',
            field=models.IntegerField(default=0, verbose_name='Quantité Commandé'),
        ),
        migrations.AlterField(
            model_name='commande',
            name='quantite_recue',
            field=models.IntegerField(default=0, verbose_name='Quantité Reçue'),
        ),
    ]