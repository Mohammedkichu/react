# Generated by Django 2.2.28 on 2023-05-11 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medicine', '0002_rename_medicine_name_medicine_mname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medicine',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]