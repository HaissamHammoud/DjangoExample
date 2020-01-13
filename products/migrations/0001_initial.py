# Generated by Django 3.0.2 on 2020-01-13 21:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('description', models.TextField(blank=True, null=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('summary', models.TextField(default='this is cool', null=True)),
                ('featured', models.BooleanField(default=True)),
                ('stock', models.IntegerField(default=0)),
            ],
        ),
    ]
