# Generated by Django 5.2.1 on 2025-05-21 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rentals', '0005_remove_campervanimage_url_campervanimage_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='campervan',
            name='description_de',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='campervan',
            name='description_en',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='campervan',
            name='name_de',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='campervan',
            name='name_en',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
