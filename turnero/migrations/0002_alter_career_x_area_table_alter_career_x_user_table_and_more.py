# Generated by Django 4.2.1 on 2023-06-05 22:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('turnero', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='career_x_area',
            table='careers_x_areas',
        ),
        migrations.AlterModelTable(
            name='career_x_user',
            table='career_x_users',
        ),
        migrations.AlterModelTable(
            name='postulation_x_area',
            table='postulations_x_areas',
        ),
        migrations.AlterModelTable(
            name='user_x_area',
            table='users_x_areas',
        ),
        migrations.AlterModelTable(
            name='user_x_role',
            table='users_x_roles',
        ),
        migrations.AlterModelTable(
            name='user_x_tutorship_instance_x_role',
            table='users_x_tutorship_instances_x_roles',
        ),
    ]
