# Generated by Django 3.2.9 on 2021-11-11 11:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('album', '0002_auto_20211110_1533'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='pages_count',
            new_name='pagesCount',
        ),
        migrations.RemoveField(
            model_name='order',
            name='date',
        ),
        migrations.RemoveField(
            model_name='order',
            name='number',
        ),
        migrations.AddField(
            model_name='order',
            name='pagesType',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='album.page'),
        ),
    ]
