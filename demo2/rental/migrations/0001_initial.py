# Generated by Django 3.0.4 on 2020-03-13 06:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Library',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Borrowed',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bookdate', models.DateTimeField(auto_now_add=True)),
                ('mybook', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rental.Library')),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rental.Student')),
            ],
        ),
    ]