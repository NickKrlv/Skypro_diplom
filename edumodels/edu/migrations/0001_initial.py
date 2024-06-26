# Generated by Django 5.0.4 on 2024-04-29 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EduModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField(db_index=True, unique=True, verbose_name='Номер модели')),
                ('name', models.CharField(db_index=True, max_length=30, unique=True, verbose_name='Название модели')),
                ('description', models.TextField(verbose_name='Описание модели')),
            ],
            options={
                'verbose_name': 'Модель',
                'verbose_name_plural': 'Модели',
                'ordering': ['number'],
            },
        ),
    ]
