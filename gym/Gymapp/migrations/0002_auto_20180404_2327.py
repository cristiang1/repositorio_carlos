# Generated by Django 2.0.4 on 2018-04-05 04:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Gymapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='usuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('ejercicio', models.ManyToManyField(blank=True, null=True, to='Gymapp.ejercicio')),
            ],
        ),
        migrations.RemoveField(
            model_name='gym',
            name='ejercicio',
        ),
        migrations.RemoveField(
            model_name='gym',
            name='horarios',
        ),
        migrations.RemoveField(
            model_name='gym',
            name='recepcionista',
        ),
        migrations.AddField(
            model_name='usuario',
            name='gym',
            field=models.ManyToManyField(blank=True, null=True, to='Gymapp.gym'),
        ),
        migrations.AddField(
            model_name='usuario',
            name='horarios',
            field=models.ManyToManyField(blank=True, null=True, to='Gymapp.horario'),
        ),
        migrations.AddField(
            model_name='usuario',
            name='recepcionista',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Gymapp.recepcionista'),
        ),
    ]
