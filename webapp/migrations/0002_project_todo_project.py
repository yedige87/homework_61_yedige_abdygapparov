# Generated by Django 4.1.6 on 2023-03-10 12:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project', models.CharField(max_length=50, verbose_name='Проект')),
                ('text', models.TextField(max_length=2000, verbose_name='Описание')),
                ('date_start', models.CharField(max_length=20, verbose_name='Начало')),
                ('date_end', models.CharField(max_length=20, verbose_name='Завершение')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата и время создания')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Дата и время изменения')),
            ],
        ),
        migrations.AddField(
            model_name='todo',
            name='project',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, related_name='todo', to='webapp.project', verbose_name='Project'),
        ),
    ]
