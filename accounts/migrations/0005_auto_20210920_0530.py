# Generated by Django 3.2.7 on 2021-09-20 05:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20210918_0547'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='type',
        ),
        migrations.AddField(
            model_name='customuser',
            name='user_type',
            field=models.CharField(choices=[(1, 'employer'), (2, 'jobseeker')], default=2, max_length=255),
        ),
        migrations.CreateModel(
            name='Jobseeker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Employer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('org_name', models.CharField(max_length=255)),
                ('email', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
