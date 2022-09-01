# Generated by Django 4.1 on 2022-09-01 06:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0003_rename_descriptions_comment_description_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=250, null=True, verbose_name='Subject')),
                ('body', models.TextField(verbose_name='Body')),
            ],
        ),
    ]