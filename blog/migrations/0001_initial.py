# Generated by Django 5.1.1 on 2024-11-03 07:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Free',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('bio', models.TextField()),
                ('price', models.IntegerField()),
                ('img', models.ImageField(upload_to='free/')),
            ],
        ),
    ]
