# Generated by Django 3.0.6 on 2020-05-12 17:02

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Publicacao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_publicacao', models.CharField(max_length=200)),
                ('descricao', models.TextField()),
                ('categoria', models.CharField(max_length=100)),
                ('preco', models.FloatField()),
                ('data_receita', models.DateField(blank=True, default=datetime.datetime.now)),
                ('publicada', models.BooleanField(default=False)),
                ('foto_receita', models.ImageField(blank=True, upload_to='fotos/%d/%m/%Y')),
            ],
        ),
    ]
