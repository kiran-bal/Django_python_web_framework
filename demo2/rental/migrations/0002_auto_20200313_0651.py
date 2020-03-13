# Generated by Django 3.0.4 on 2020-03-13 06:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rental', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='borrowed',
            name='returndate',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='library',
            name='author',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='student',
            name='college',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]