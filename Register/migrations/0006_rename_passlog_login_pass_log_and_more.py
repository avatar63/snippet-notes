# Generated by Django 4.0.6 on 2022-09-20 13:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Register', '0005_rename_password_login_passlog_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='login',
            old_name='passlog',
            new_name='pass_log',
        ),
        migrations.RenameField(
            model_name='login',
            old_name='userlog',
            new_name='user_log',
        ),
    ]
