# Generated by Django 4.0.5 on 2024-04-18 09:26

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('books', '0003_alter_books_users'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='users',
            field=models.ManyToManyField(related_name='books', to=settings.AUTH_USER_MODEL),
        ),
    ]
