# Generated by Django 4.0.6 on 2022-07-18 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0019_blogsingle'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogDavis',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='BlogDavis name')),
                ('about', models.TextField(verbose_name='BlogDavis about')),
                ('img', models.ImageField(upload_to='media', verbose_name='BlogDavis image')),
            ],
            options={
                'verbose_name': 'BlogDavis',
                'verbose_name_plural': 'BlogsDavis',
            },
        ),
    ]