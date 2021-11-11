# Generated by Django 3.2.9 on 2021-11-10 12:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Buyer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('surname', models.CharField(max_length=50)),
                ('number', models.CharField(max_length=12)),
                # ('avatar', models.ImageField(null=True, upload_to='uploads/', verbose_name='Avatar')),
            ],
        ),
        migrations.CreateModel(
            name='Cover',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cover', models.CharField(db_index=True, max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('page', models.CharField(db_index=True, max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Pattern',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pattern', models.CharField(db_index=True, max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Size',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size', models.CharField(db_index=True, max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=500)),
                ('buyer', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='album.buyer')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=10)),
                ('pages_count', models.IntegerField()),
                ('date', models.DateTimeField()),
                ('status', models.CharField(max_length=15)),
                ('buyer', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='album.buyer')),
                ('cover', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='album.cover')),
                ('pattern', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='album.pattern')),
                ('size', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='album.size')),
            ],
        ),
    ]
