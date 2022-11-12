# Generated by Django 4.0.1 on 2022-11-10 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('commande', '0002_alter_commande_options_alter_commande_date_commande_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='LigneCommande',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num_cmd', models.IntegerField(verbose_name='N° de commande')),
            ],
            options={
                'ordering': ['-num_cmd'],
            },
        ),
        migrations.AlterField(
            model_name='commande',
            name='ecart',
            field=models.CharField(max_length=200, verbose_name='Ecart'),
        ),
    ]
