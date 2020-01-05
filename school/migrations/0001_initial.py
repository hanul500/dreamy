# Generated by Django 3.0.1 on 2020-01-03 18:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Schoolinfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sch_code', models.CharField(blank=True, max_length=120, null=True)),
                ('sch_id', models.CharField(blank=True, max_length=120, null=True)),
                ('sch_name', models.CharField(blank=True, max_length=120, null=True)),
                ('sch_email', models.CharField(blank=True, max_length=120, null=True)),
                ('sch_address', models.CharField(blank=True, max_length=120, null=True)),
                ('sch_tel', models.CharField(blank=True, max_length=120, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Schoolteainfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('schtea_id', models.CharField(blank=True, max_length=120, null=True)),
                ('schtea_name', models.CharField(blank=True, max_length=120, null=True)),
                ('schtea_email', models.CharField(blank=True, max_length=120, null=True)),
                ('schtea_pos', models.CharField(blank=True, max_length=120, null=True)),
                ('schtea_tel1', models.CharField(blank=True, max_length=120, null=True)),
                ('schtea_tel2', models.CharField(blank=True, max_length=120, null=True)),
                ('schtea_tel3', models.CharField(blank=True, max_length=120, null=True)),
                ('schtea_schkey', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='school.Schoolinfo')),
            ],
        ),
    ]