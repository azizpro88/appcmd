# Generated by Django 4.0.1 on 2022-11-10 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('commande', '0005_rename_num_cmd_commande_lignecommande'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commande',
            name='ecart',
            field=models.CharField(max_length=200, null=True, verbose_name='Ecart'),
        ),
    ]
