# Generated by Django 2.2.3 on 2019-07-27 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0005_auto_20190727_1350'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ideia',
            name='titulo',
            field=models.CharField(max_length=255, unique=True, verbose_name='Noma da Ideia'),
        ),
    ]