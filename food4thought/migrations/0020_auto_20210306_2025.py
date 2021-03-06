# Generated by Django 3.1.6 on 2021-03-06 20:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food4thought', '0019_auto_20210303_0959'),
    ]

    operations = [
        migrations.CreateModel(
            name='Thought',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('author', models.CharField(max_length=100)),
                ('bible_quotations', models.CharField(max_length=500)),
                ('views', models.IntegerField(blank=True, default=0)),
                ('audio_content', models.FileField(blank=True, help_text='select audio content', upload_to='post_audio_files')),
                ('date_posted', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Post',
        ),
    ]
