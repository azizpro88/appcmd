# Generated by Django 4.0.1 on 2022-11-10 18:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('commande', '0003_lignecommande_alter_commande_ecart'),
    ]

    operations = [
        migrations.AddField(
            model_name='commande',
            name='num_cmd',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='commande.lignecommande'),
            preserve_default=False,
        ),
    ]
