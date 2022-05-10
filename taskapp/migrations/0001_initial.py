# Generated by Django 4.0.4 on 2022-05-07 02:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1000, verbose_name='Task Name')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='Created Date')),
                ('completed', models.BooleanField(default=False)),
                ('completed_date', models.DateTimeField(verbose_name='Completed Date')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
