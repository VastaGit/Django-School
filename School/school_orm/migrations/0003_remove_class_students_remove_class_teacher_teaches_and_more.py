# Generated by Django 4.2 on 2023-06-27 09:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('school_orm', '0002_class_remove_student_subject_school_classes_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='class',
            name='students',
        ),
        migrations.RemoveField(
            model_name='class',
            name='teacher',
        ),
        migrations.CreateModel(
            name='Teaches',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('class_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school_orm.class')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='teachers', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Studies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('class_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school_orm.class')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='students', to='school_orm.student')),
            ],
        ),
        migrations.AddField(
            model_name='student',
            name='studies',
            field=models.ManyToManyField(through='school_orm.Studies', to='school_orm.class'),
        ),
        migrations.AddField(
            model_name='teacher',
            name='teaches',
            field=models.ManyToManyField(through='school_orm.Teaches', to='school_orm.class'),
        ),
    ]
