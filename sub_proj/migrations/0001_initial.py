# Generated by Django 4.0.1 on 2022-01-31 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=50)),
                ('username', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=12)),
            ],
        ),
    ]