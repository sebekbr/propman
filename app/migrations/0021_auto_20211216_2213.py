# Generated by Django 3.2.8 on 2021-12-16 21:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0020_leaseagreement_type'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='leaseagreement_type',
            options={'ordering': ['id']},
        ),
        migrations.AlterField(
            model_name='leaseagreement',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.leaseagreement_type'),
        ),
    ]
