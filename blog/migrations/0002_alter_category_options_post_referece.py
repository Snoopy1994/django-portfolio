# Generated by Django 4.2 on 2024-01-08 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'categories'},
        ),
        migrations.AddField(
            model_name='post',
            name='referece',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
