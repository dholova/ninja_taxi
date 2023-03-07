# Generated by Django 4.1.7 on 2023-03-04 08:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=200, unique=True)),
                ('phone', models.CharField(max_length=20)),
                ('car_in_fleet', models.CharField(max_length=255)),
                ('confirmed', models.BooleanField(default=False)),
                ('language', models.CharField(max_length=255)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=100)),
                ('city', models.CharField(default='Kyiv', max_length=255)),
                ('language_2', models.CharField(default='Ukrainian', max_length=255)),
                ('billing_type', models.CharField(default='Company', max_length=255)),
                ('company_name', models.CharField(default='', max_length=250)),
                ('address', models.CharField(default='', max_length=250)),
                ('registration_code', models.CharField(default='', max_length=50)),
                ('vat_liability', models.CharField(default='', max_length=20)),
                ('vat_number', models.CharField(default='', max_length=50)),
                ('bank_acc_holder_name', models.CharField(default='', max_length=50)),
                ('bank_acc', models.CharField(default='', max_length=50)),
                ('bic_swift', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=150)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
