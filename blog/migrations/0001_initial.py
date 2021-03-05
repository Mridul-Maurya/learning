# Generated by Django 2.1 on 2019-04-05 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='images/')),
                ('pub_date', models.DateField()),
                ('name', models.CharField(max_length=30)),
                ('body', models.TextField(help_text='Enter a brief description of the course', max_length=2000)),
            ],
        ),
    ]
