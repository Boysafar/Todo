# Generated by Django 5.0.6 on 2024-07-05 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Ish nomi ')),
                ('description', models.TextField(verbose_name='Tafsiv')),
                ('status', models.CharField(choices=[('new', 'Yangi'), ('in_process', 'Jarayonda'), ('done', 'Bajarildi'), ('canceled', 'Bekor qilindi')], max_length=10, verbose_name='Holati')),
            ],
        ),
    ]
