# Generated by Django 4.2.7 on 2023-12-05 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0003_alter_usuario_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='username',
            field=models.CharField(max_length=150, verbose_name='username'),
        ),
    ]
