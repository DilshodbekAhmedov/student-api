# Generated by Django 4.2.5 on 2023-10-04 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appd', '0002_alter_teacher_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='status',
            field=models.BooleanField(default=False),
        ),
    ]