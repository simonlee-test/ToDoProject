# Generated by Django 5.0.7 on 2024-07-26 06:48

import uuid
from django.db import migrations, models
from django.template.defaultfilters import slugify

class Migration(migrations.Migration):

    dependencies = [
        ('ToDoList', '0004_alter_task_options_tasklist_slug_and_more'),
    ]
    
    def gen_slug(apps, schema_editor):
        MyModel = apps.get_model("ToDoList", "TaskList")
        for row in MyModel.objects.all():
            row.slug = slugify(row.title)
            row.save(update_fields=["slug"])

    operations = [
        migrations.AlterField(
            model_name='tasklist',
            name='slug',
            field=models.SlugField(default=uuid.uuid4, max_length=100, unique=True),
        ),
        migrations.RunPython(gen_slug, reverse_code=migrations.RunPython.noop),
    ]