# Generated by Django 3.1.6 on 2021-03-08 19:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food4thought', '0021_auto_20210308_1912'),
    ]

    operations = [
        migrations.AddField(
            model_name='becomemember',
            name='profession',
            field=models.CharField(blank=True, help_text="If can leave this field blank if you don't to your profession", max_length=100),
        ),
    ]
