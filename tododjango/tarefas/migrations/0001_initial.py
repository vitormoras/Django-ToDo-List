# Generated by Django 5.1.7 on 2025-03-19 23:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tarefa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tarefa', models.CharField(max_length=200)),
                ('data', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
