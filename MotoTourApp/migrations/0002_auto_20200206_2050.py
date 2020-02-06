# Generated by Django 2.2.9 on 2020-02-06 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MotoTourApp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='message',
        ),
        migrations.RemoveField(
            model_name='post',
            name='title',
        ),
        migrations.AddField(
            model_name='post',
            name='age',
            field=models.CharField(default=0, help_text='age du participant', max_length=120),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='cylindré',
            field=models.CharField(default=0, help_text='cylindré de la moto', max_length=120),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='kilometrage',
            field=models.CharField(default=0, help_text='kilometrage de la moto', max_length=120),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='marque_moto',
            field=models.CharField(default=0, help_text='marque de la moto', max_length=120),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='nom',
            field=models.CharField(default=0, help_text='Nom du participant', max_length=120),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='prenom',
            field=models.CharField(default=0, help_text='Prenom du participant', max_length=120),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='sexe',
            field=models.CharField(default=0, help_text='sexe du participant', max_length=120),
            preserve_default=False,
        ),
    ]
