# Generated by Django 2.2.12 on 2020-05-16 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0010_remove_imagemodel_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='imagemodel',
            name='name',
            field=models.CharField(default='', max_length=35, verbose_name='Имя'),
            preserve_default=False,
        ),
    ]
