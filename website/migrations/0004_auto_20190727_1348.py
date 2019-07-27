# Generated by Django 2.2.3 on 2019-07-27 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_ideia'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ideia',
            old_name='categoria_outros',
            new_name='categorias_outros',
        ),
        migrations.AlterField(
            model_name='ideia',
            name='categorias',
            field=models.CharField(choices=[('TERRA_PLANA', 'Terra Plana'), ('CONTRA_GROGER', 'Ideias para Coach Groger'), ('CONTRA_JOAO', 'Ideias contra João'), ('PUBLICAS', 'Públicas'), ('OUTROS', 'Outros')], max_length=255, verbose_name='Categorias'),
        ),
        migrations.AlterField(
            model_name='ideia',
            name='titulo',
            field=models.TextField(max_length=255, unique=True, verbose_name='Noma da Ideia'),
        ),
    ]
