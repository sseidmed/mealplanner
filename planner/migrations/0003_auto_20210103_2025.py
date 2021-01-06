# Generated by Django 3.1.3 on 2021-01-03 20:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('planner', '0002_meal_cook'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='meal',
            name='cook',
        ),
        migrations.AddField(
            model_name='day',
            name='cook',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
            preserve_default=False,
        ),
    ]
