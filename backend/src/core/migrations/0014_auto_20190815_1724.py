# Generated by Django 2.2.3 on 2019-08-15 11:54

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_auto_20190815_1604'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='content',
            field=tinymce.models.HTMLField(default='test'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='post',
            name='overview',
            field=models.TextField(),
        ),
    ]
