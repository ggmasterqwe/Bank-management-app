# Generated by Django 3.1.2 on 2020-10-19 14:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('baseuser', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BranchAdmin',
            fields=[
                ('mainuser_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='baseuser.mainuser')),
                ('date_employed', models.DateField(auto_now_add=True, null=True)),
                ('salary', models.BigIntegerField(blank=True, null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('baseuser.mainuser',),
        ),
        migrations.CreateModel(
            name='Branch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=45)),
                ('telephone', models.CharField(max_length=11)),
                ('admin', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='branch_admin', to='branches.branchadmin')),
            ],
        ),
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account_number', models.CharField(blank=True, max_length=12, null=True, unique=True)),
                ('is_closed', models.BooleanField(default=False)),
                ('date_added', models.DateField(auto_now=True, null=True)),
                ('branch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='branch_account', to='branches.branch')),
                ('client', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='bank_account', to='baseuser.client')),
            ],
        ),
    ]
