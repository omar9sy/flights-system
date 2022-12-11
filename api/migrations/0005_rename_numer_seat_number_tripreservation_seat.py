# Generated by Django 4.1.3 on 2022-12-10 23:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_tripreservation'),
    ]

    operations = [
        migrations.RenameField(
            model_name='seat',
            old_name='numer',
            new_name='number',
        ),
        migrations.AddField(
            model_name='tripreservation',
            name='seat',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='seat', to='api.seat'),
            preserve_default=False,
        ),
    ]