# Generated by Django 3.0.7 on 2020-08-10 02:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0006_auto_20200810_0206'),
    ]

    operations = [
        migrations.AlterField(
            model_name='download_time',
            name='card',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quiz.Card'),
        ),
    ]
