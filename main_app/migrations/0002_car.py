# Generated by Django 4.1.1 on 2022-10-06 15:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('make', models.CharField(max_length=50)),
                ('model', models.CharField(max_length=50)),
                ('chasis', models.CharField(max_length=50)),
                ('finch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cars', to='main_app.finch')),
            ],
        ),
    ]
