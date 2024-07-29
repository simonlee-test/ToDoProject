# Generated by Django 5.0.7 on 2024-07-29 02:20

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TaskList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, unique=True)),
                ('slug', models.SlugField(default='', editable=False, max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('created_datetime', models.DateTimeField(auto_now_add=True)),
                ('due_datetime', models.DateTimeField(blank=True, verbose_name='due date & time')),
                ('is_done', models.BooleanField(default=False)),
                ('tasklist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tasks', to='ToDoList.tasklist')),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
    ]
