# Generated by Django 4.2.1 on 2023-06-05 22:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('turnero', '0002_alter_career_x_area_table_alter_career_x_user_table_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='ucc_key',
            field=models.PositiveIntegerField(null=True),
        ),
    ]
