# Generated by Django 2.2.7 on 2019-11-11 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Bio', models.CharField(max_length=255)),
                ('maintenance_mode', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Bio',
                'verbose_name_plural': 'Bio',
            },
        ),
        migrations.AlterModelOptions(
            name='gostos',
            options={'ordering': ['gosto'], 'verbose_name': 'o que você gosta', 'verbose_name_plural': 'Gostos'},
        ),
        migrations.AlterField(
            model_name='gostos',
            name='gosto',
            field=models.CharField(max_length=50, verbose_name='Gosto de...'),
        ),
    ]
