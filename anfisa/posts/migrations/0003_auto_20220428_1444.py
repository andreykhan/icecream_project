# Generated by Django 2.2.19 on 2022-04-28 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_auto_20220425_2135'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='slug',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='post',
            name='pub_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
