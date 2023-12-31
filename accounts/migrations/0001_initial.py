# Generated by Django 3.1 on 2021-05-18 11:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Accounts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mobile', models.BigIntegerField()),
                ('gender', models.IntegerField(choices=[(0, 'MALE'), (1, 'FEMALE'), (2, 'OTHER')], default=0)),
                ('dob', models.DateField()),
                ('address', models.TextField(blank=True, null=True)),
                ('userstatus', models.IntegerField(choices=[(1, 'Registration Completed'), (2, 'Account UnderReview'), (3, 'Accounts Verified')], default=1)),
                ('total_amount', models.DecimalField(decimal_places=3, default=0.0, max_digits=10)),
                ('remaining_amount', models.DecimalField(decimal_places=3, default=0.0, max_digits=10)),
                ('used_amount', models.DecimalField(decimal_places=3, default=0.0, max_digits=10)),
                ('skypeid', models.CharField(blank=True, max_length=100, null=True)),
                ('key', models.CharField(blank=True, max_length=30, null=True)),
                ('is_api_enabled', models.BooleanField(default=False)),
                ('userrole', models.IntegerField(choices=[(1, 'Super Admin'), (2, 'Doctor'), (3, 'Patient')], default=4)),
                ('parentuser', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='parentuser', to=settings.AUTH_USER_MODEL)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='userdetail', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
