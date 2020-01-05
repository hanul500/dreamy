# Generated by Django 3.0.1 on 2020-01-03 18:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('material', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Classstatinfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('class_code', models.CharField(max_length=120)),
                ('recipe_cate', models.CharField(max_length=120)),
                ('class_title', models.CharField(blank=True, max_length=120)),
                ('class_detail', models.TextField(blank=True, null=True)),
                ('recipe_mat', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='material.Materialinfo')),
                ('recipe_tool', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='material.Toolinfo')),
            ],
        ),
        migrations.CreateModel(
            name='stat_tool_rel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stat_mat_num', models.CharField(blank=True, max_length=120, null=True)),
                ('stat_tool', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='classstatd.Classstatinfo')),
                ('tool_stat', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='material.Toolinfo')),
            ],
        ),
        migrations.CreateModel(
            name='stat_mat_rel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stat_mat_num', models.CharField(blank=True, max_length=120, null=True)),
                ('mat_stat', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='material.Materialinfo')),
                ('stat_mat', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='classstatd.Classstatinfo')),
            ],
        ),
    ]
