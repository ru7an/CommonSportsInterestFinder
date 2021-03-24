# Generated by Django 3.0.8 on 2021-03-23 08:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user_data',
            name='id',
        ),
        migrations.AlterField(
            model_name='user_data',
            name='email',
            field=models.EmailField(default=False, max_length=254, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='user_data',
            name='profile',
            field=models.ImageField(default='default_profile.jpg', upload_to='user_profile'),
        ),
    ]