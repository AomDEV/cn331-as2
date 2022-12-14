# Generated by Django 4.1.1 on 2022-09-17 10:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('assignment', '0005_alter_user_last_login_alter_user_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subject',
            name='enroll',
            field=models.ManyToManyField(blank=True, related_name='enroll', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='subject',
            name='teacher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='teacher', to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
