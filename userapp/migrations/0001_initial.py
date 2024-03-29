# Generated by Django 3.2.23 on 2024-02-15 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Auditrequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('useremail', models.EmailField(max_length=254, null=True)),
                ('fileid', models.CharField(max_length=20, null=True)),
                ('filename', models.CharField(max_length=20, null=True)),
                ('requested_date', models.DateTimeField(auto_now_add=True)),
                ('proofcheck', models.CharField(default='waiting', max_length=20, null=True)),
                ('status', models.CharField(default='waiting', max_length=20, null=True)),
            ],
            options={
                'db_table': 'Auditrequest',
            },
        ),
        migrations.CreateModel(
            name='Uploadfiles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_email', models.CharField(max_length=50, null=True)),
                ('inputfilename', models.CharField(max_length=50, null=True)),
                ('filename', models.CharField(max_length=50, null=True)),
                ('uploadeddate', models.DateTimeField(auto_now_add=True)),
                ('hashcodeone', models.TextField(null=True)),
                ('hashcodetwo', models.TextField(null=True)),
                ('hashcodethree', models.TextField(null=True)),
                ('hashcodefour', models.TextField(null=True)),
                ('keyone', models.TextField(null=True)),
                ('keytwo', models.TextField(null=True)),
                ('keythree', models.TextField(null=True)),
                ('keyfour', models.TextField(null=True)),
            ],
            options={
                'db_table': 'Uploadfiles',
            },
        ),
        migrations.CreateModel(
            name='Userregister',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=50, null=True)),
                ('user_email', models.EmailField(max_length=254, null=True)),
                ('user_contact', models.CharField(max_length=10, null=True)),
                ('user_address', models.CharField(max_length=100, null=True)),
                ('user_password', models.CharField(max_length=50, null=True)),
                ('registered_date', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(default='pending', max_length=20, null=True)),
            ],
            options={
                'db_table': 'Userregister',
            },
        ),
    ]
